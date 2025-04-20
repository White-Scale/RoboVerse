from metasim.cfg.checkers import DetectedChecker, RelativeBboxDetector
from metasim.cfg.objects import PrimitiveCubeCfg
from metasim.constants import PhysicStateType
from metasim.utils import configclass

from .maniskill_task_cfg import ManiskillTaskCfg


@configclass
class StackCubeCustomCfg(ManiskillTaskCfg):
    """The stack cube task from ManiSkill.

    The robot is tasked to pick up a cube and stack it on another cube.
    """

    episode_length = 250
    objects = [
        PrimitiveCubeCfg(
            name="cubeA",
            size=[0.04, 0.04, 0.04],
            mass=0.02,
            physics=PhysicStateType.RIGIDBODY,
            color=[0.0, 1.0, 0.0],
            mjcf_path="roboverse_data/assets/maniskill/cube/cube.mjcf",
        ),
        PrimitiveCubeCfg(
            name="cubeB",
            size=[0.04, 0.04, 0.04],
            mass=0.02,
            physics=PhysicStateType.RIGIDBODY,
            color=[0.0, 0.0, 1.0],
            mjcf_path="roboverse_data/assets/maniskill/cube/base.mjcf",
        ),
    ]
    traj_filepath = "/home/spyder/Maniskill-dp3/converted_output_v2.pkl"

    ## TODO: detect velocity
    checker = DetectedChecker(
        obj_name="cubeA",
        detector=RelativeBboxDetector(
            base_obj_name="cubeB",
            relative_pos=(0.0, 0.0, 0.04),
            relative_quat=(1.0, 0.0, 0.0, 0.0),
            checker_lower=(-0.02, -0.02, -0.02),
            checker_upper=(0.02, 0.02, 0.02),
            ignore_base_ori=True,
        ),
    )
