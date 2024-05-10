#  Copyright (c) 2020 the original author or authors
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.

import logging

from src.services.utils.pyutils import get_env, get_env_split, get_env_bool, Constants

_DEFAULT_SCANNER = 'Facenet2018'


class ENV(Constants):
    ML_PORT = int(get_env('ML_PORT', '3000'))
    IMG_LENGTH_LIMIT = int(get_env('IMG_LENGTH_LIMIT', '640'))

    #FACE_DETECTION_PLUGIN = get_env('FACE_DETECTION_PLUGIN', 'facenet.FaceDetector')
    FACE_DETECTION_PLUGIN = get_env('FACE_DETECTION_PLUGIN', 'insightface.FaceDetector@retinaface_mnet025_v1')

    CALCULATION_PLUGIN = get_env('CALCULATION_PLUGIN', 'insightface.Calculator@arcface_mobilefacenet')
    #CALCULATION_PLUGIN = get_env('CALCULATION_PLUGIN', 'facenet.Calculator')
    EXTRA_PLUGINS = get_env_split('EXTRA_PLUGINS', 'facenet.LandmarksDetector,agegender.AgeDetector,agegender.GenderDetector,facenet.facemask.MaskDetector,facenet.PoseEstimator')

    LOGGING_LEVEL_NAME = get_env('LOGGING_LEVEL_NAME', 'debug').upper()
    IS_DEV_ENV = get_env('FLASK_ENV', 'production') == 'development'
    BUILD_VERSION = get_env('APP_VERSION_STRING', 'dev')

    ###
    #GPU_IDX = int(get_env('GPU_IDX', '-1'))
    ####

    INTEL_OPTIMIZATION = get_env_bool('INTEL_OPTIMIZATION')

    RUN_MODE = get_env_bool('RUN_MODE', False)

    # PyTorch settings
    PYTORCH_MODE = get_env_bool('PYTORCH_MODE', True)  # True or False
    DEVICE = get_env('DEVICE', 'cpu') # 'cpu' or 'cuda:0'
    RECOGNITION_MODEL = get_env('RECOGNITION_MODEL', 'ir_50')
    RECOGNITION_MODEL_PATH = get_env('RECOGNITION_MODEL_PATH', 'src/services/facescan/plugins/adaface/pretrained/adaface_ir101_webface4m.ckpt')
    DETECTOR_NAME = get_env('DETECTOR_NAME', 'retinaface') # mtcnn or retinaface
    DETECTOR_NETWORK_NAME = get_env('DETECTOR_NETWORK_NAME', 'resnet50') # 'mobile0.25' or 'resnet50'
    DETECTOR_MODEL_PATH = get_env('DETECTOR_MODEL_PATH', 'src/services/facescan/plugins/pytorch_detector/weights/mobilenet0.25_Final.pth')
    PRETRAINED_MODEL_PATH = get_env('PRETRAINED_MODEL_PATH', 'src/services/facescan/plugins/pytorch_detector/weights/mobilenetV1X0.25_pretrain.tar')

LOGGING_LEVEL = logging._nameToLevel[ENV.LOGGING_LEVEL_NAME]
ENV_MAIN = ENV
SKIPPED_PLUGINS = ["insightface.PoseEstimator", "facemask.MaskDetector", "facenet.PoseEstimator"]
