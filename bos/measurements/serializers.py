#  Copyright (c) 2019 Maverick Labs
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as,
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer
from measurements.models import Measurement, MeasurementType
from ngos.models import NGO


class MeasurementSerializer(ModelSerializer):
    lookup_field = 'key'
    pk_field = 'key'
    ngo = SlugRelatedField(slug_field='key', queryset=NGO.objects.all())
    types = SlugRelatedField(slug_field='key', queryset=MeasurementType.objects.all(), many=True)

    class Meta:
        model = Measurement
        exclude = ('id',)


class MeasurementTypeSerializer(ModelSerializer):
    lookup_field = 'key'
    pk_field = 'key'
    ngo = SlugRelatedField(slug_field='key', queryset=NGO.objects.all())

    class Meta:
        model = MeasurementType
        exclude = ('id',)


class MeasurementDetailSerializer(ModelSerializer):
    lookup_field = 'key'
    pk_field = 'key'
    ngo = SlugRelatedField(slug_field='key',read_only=True)
    types = MeasurementTypeSerializer(many=True,read_only=True)

    class Meta:
        model = Measurement
        exclude = ('id',)
