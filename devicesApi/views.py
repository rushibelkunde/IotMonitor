from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
# views.py
from datetime import datetime
from rest_framework import generics
from .models import Device, TemperatureReading, HumidityReading
from .serializers import DeviceSerializer, TemperatureReadingSerializer, HumidityReadingSerializer
from django.shortcuts import get_object_or_404, get_list_or_404

# landing page
def Home(request):
    return render(request, "home.html")


# api functions
# Get all Devices using GET and Create Device using POST request
@api_view(["GET", "POST"])
def CreateDevice(request):
    if request.method == "GET":
        devices = get_list_or_404(Device)
        # return Response(data=devices)
        serializer = DeviceSerializer(devices, many= True)
        return Response({"All Devices" :serializer.data})
    
    elif request.method == "POST":
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


# Get Specific device by uid and Delete 
@api_view(["GET", "DELETE"])
def GetDevice(request, uid):
    device = get_object_or_404(Device, uid=uid)

    if request.method == "GET":
        serializer = DeviceSerializer(device)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        device.delete()
        return Response({"message": "Device deleted successfully"})


# Get Readings of Devices 
@api_view(["GET"])
def ReadingView(request, uid, parameter):
     # Get the device
    device = get_object_or_404(Device, uid=uid)

    # Get start_on and end_on from query parameters
    start_on = request.GET.get('start_on')
    end_on = request.GET.get('end_on')

    # Convert start_on and end_on to datetime objects
    start_datetime = datetime.strptime(start_on, '%Y-%m-%dT%H:%M:%S')
    end_datetime = datetime.strptime(end_on, '%Y-%m-%dT%H:%M:%S')

    if parameter == 'temperature':
        ReadingModel = TemperatureReading
        SerializerClass = TemperatureReadingSerializer
    elif parameter == 'humidity':
        ReadingModel = HumidityReading
        SerializerClass = HumidityReadingSerializer
    else:
        return Response({'error': 'Invalid parameter'}, status=400)
    # Query readings for the device within the specified time range
    readings = ReadingModel.objects.filter(
        device=device,
        timestamp__gte=start_datetime,
        timestamp__lte=end_datetime
    )
    # Serialize the readings
    serializer = SerializerClass(readings, many=True)
    # Return the serialized data
    return Response(serializer.data)


# Render Graph 
def DeviceGraphView(request, uid):
     # Get the device
    device = Device.objects.get(uid=uid)

    # Get temperature and humidity readings for the device
    temperature_readings = TemperatureReading.objects.filter(device=device)
    humidity_readings = HumidityReading.objects.filter(device=device)

    # Prepare data for plotting
    temperature_data = [{'x': reading.timestamp, 'y': reading.temperature} for reading in temperature_readings]
    humidity_data = [{'x': reading.timestamp, 'y': reading.humidity} for reading in humidity_readings]

    # Pass data to the template
    context = {
        'device_name': device.name,
        'temperature_data': temperature_data,
        'humidity_data': humidity_data,
    }

    return render(request, 'graph.html', context)






