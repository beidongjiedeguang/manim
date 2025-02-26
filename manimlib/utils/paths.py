import numpy as np
import math

from ..constants import OUT
from ..utils.bezier import interpolate
from ..utils.space_ops import get_norm
from ..utils.space_ops import rotation_matrix_transpose

STRAIGHT_PATH_THRESHOLD = 0.01


def straight_path(start_points, end_points, alpha):
    """
    Same function as interpolate, but renamed to reflect
    intent of being used to determine how a set of points move
    to another set.  For instance, it should be a specific case
    of path_along_arc
    """
    return interpolate(start_points, end_points, alpha)


def path_along_arc(arc_angle, axis=OUT):
    """
    If vect is vector from start to end, [vect[:,1], -vect[:,0]] is
    perpendicular to vect in the left direction.
    """
    if abs(arc_angle) < STRAIGHT_PATH_THRESHOLD:
        return straight_path
    if get_norm(axis) == 0:
        axis = OUT
    unit_axis = axis / get_norm(axis)

    def path(start_points, end_points, alpha):
        vects = end_points - start_points
        centers = start_points + 0.5 * vects
        if arc_angle != np.pi:
            centers += np.cross(unit_axis, vects / 2.0) / math.tan(arc_angle / 2)
        rot_matrix_T = rotation_matrix_transpose(alpha * arc_angle, unit_axis)
        return centers + np.dot(start_points - centers, rot_matrix_T)

    return path


def clockwise_path():
    return path_along_arc(-np.pi)


def counterclockwise_path():
    return path_along_arc(np.pi)
