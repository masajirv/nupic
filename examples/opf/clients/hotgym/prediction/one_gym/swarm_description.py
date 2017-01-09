# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

SWARM_DESCRIPTION = {
  "includedFields": [
    {
      "fieldName": "timestamp",
      "fieldType": "datetime"
    },
    {
      "fieldName": "V13",
      "fieldType": "float",
      "maxValue": 640.932,
      "minValue": 0.0
    },
    {
      "fieldName": "V3",
      "fieldType": "float",
      "maxValue": 1063.637,
      "minValue": 0.0
    },
    #{
      #"fieldName": "V4",
      #"fieldType": "float",
      #"maxValue": 721.165,
      #"minValue": 0.0
    #},
    #{
      #"fieldName": "V5",
      #"fieldType": "float",
      #"maxValue": 1011.806,
      #"minValue": 0.0
    #},
    #{
     # "fieldName": "V6",
      #"fieldType": "float",
      #"maxValue": 32.708,
      #"minValue": 0.0
    #},
    #{
      #"fieldName": "V7",
      #"fieldType": "float",
      #"maxValue": 3812.964,
      #"minValue": 0.0
    #},
    #{
     # "fieldName": "V8",
      #"fieldType": "float",
      #"maxValue": 7,
      #"minValue": 0.0
    #},
    #{
      #"fieldName": "V9",
      #"fieldType": "float",
      #"maxValue": 1096.297,
      #"minValue": 0.0
    #},
    {
      "fieldName": "V10",
      "fieldType": "float",
      "maxValue": 640,
      "minValue": 0.0
    },

  ],
  "streamDef": {
    "info": "taiyoukou-data",
    "version": 1,
    "streams": [
      {
        "info": "taiyoukou",
        "source": "file://taiyoukou.csv",
        "columns": [
          "*"
        ]
      }
    ]
  },

  "inferenceType": "TemporalMultiStep",
  "inferenceArgs": {
    "predictionSteps": [
      1
    ],
    "predictedField": "V13"
  },
  "iterationCount": 9308,
  "swarmSize": "large"
}
