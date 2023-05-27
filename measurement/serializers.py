from rest_framework import serializers
from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(queryset = Sensor.objects.all(), source = 'sensor', write_only = True)
    image = serializers.ImageField(max_length=None, allow_empty_file=True, required=False)

    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'created_at', 'image']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only = True, many = True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

