# Copyright (c) 2020-2023, NVIDIA CORPORATION. All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto. Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#

import argparse
import sys

import carb
import omni
from omni.isaac.kit import SimulationApp

# This sample loads a usd stage and starts simulation
CONFIG = {"width": 1280, "height": 720, "sync_loads": True, "headless": False, "renderer": "RayTracedLighting"}



kit = SimulationApp(launch_config=CONFIG)
from omni.isaac.core.utils.nucleus import get_assets_root_path, is_file

# Locate Isaac Sim assets folder to load sample


usd_path = "/home/grntmtz/Desktop/pgm_project/isaac_env/project_env.usd"

# make sure the file exists before we try to open it
try:
    result = is_file(usd_path)
except:
    result = False

if result:
    omni.usd.get_context().open_stage(usd_path)
else:
    carb.log_error(
        f"the usd path {usd_path} could not be opened"
    )
    kit.close()
    sys.exit()
# Wait two frames so that stage starts loading
kit.update()
kit.update()

print("Loading stage...")
from omni.isaac.core.utils.stage import is_stage_loading
from omni.isaac.core import World

while is_stage_loading():
    kit.update()
print("Loading Complete")
omni.timeline.get_timeline_interface().play()
# Run in test mode, exit after a fixed number of steps
world = World()
world.add_physics_callback()
world.initialize_physics()

print(world)
while kit.is_running():
    # Run in realtime mode, we don't specify the step size
    kit.update()
omni.timeline.get_timeline_interface().stop()
kit.close()
