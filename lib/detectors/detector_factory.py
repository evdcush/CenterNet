from .exdet import ExdetDetector
from .ddd import DddDetector
from .ctdet import CtdetDetector
from .multi_pose import MultiPoseDetector

detector_factory = {
    "exdet": ExdetDetector,
    "ddd": DddDetector,
    "ctdet": CtdetDetector,
    "multi_pose": MultiPoseDetector,
}
