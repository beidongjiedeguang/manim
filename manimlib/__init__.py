from .constants import *
from sparrow.file_ops import yaml_load, ppath
from sparrow.color_str import rgb_string

_version_config = yaml_load(ppath("version-config.yaml", __file__))
__version__ = _version_config['version']
print(f"{rgb_string(_version_config['name'], color='#C9E8FF')} version: {rgb_string(__version__, color='#34A853')}")

from .animation.animation import *
from .animation.composition import *
from .animation.creation import *
from .animation.fading import *
from .animation.growing import *
from .animation.indication import *
from .animation.movement import *
from .animation.numbers import *
from .animation.rotation import *
from .animation.specialized import *
from .animation.transform import *
from .animation.transform_matching_parts import *
from .animation.update import *

from .camera.camera import *


from .mobject.boolean_ops import *
from .mobject.coordinate_systems import *
from .mobject.changing import *
from .mobject.frame import *
from .mobject.functions import *
from .mobject.geometry import *
from .mobject.matrix import *
from .mobject.mobject import *
from .mobject.number_line import *
from .mobject.numbers import *
from .mobject.probability import *
from .mobject.shape_matchers import *
from .mobject.svg.brace import *
from .mobject.svg.drawings import *
from .mobject.svg.svg_mobject import *
from .mobject.svg.tex_mobject import *
from .mobject.svg.text_mobject import *
from .mobject.three_dimensions import *
from .mobject.types.image_mobject import *
from .mobject.types.point_cloud_mobject import *
from .mobject.types.surface import *
from .mobject.types.vectorized_mobject import *
from .mobject.types.dot_cloud import *
from .mobject.mobject_update_utils import *
from .mobject.value_tracker import *
from .mobject.vector_field import *

from .scene.scene import *
from .scene.three_d_scene import *

from .utils.bezier import *
from .utils.color import *
from .utils.config_ops import *
from .utils.customization import *
from .utils.debug import *
from .utils.directories import *
from .utils.images import *
from .utils.iterables import *
from .utils.file_ops import *
from .utils.paths import *
from .utils.rate_functions import *
from .utils.simple_functions import *
from .utils.sounds import *
from .utils.space_ops import *
from .utils.strings import *
