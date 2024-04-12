from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    serial_node = Node(
        package="1DOF_arm_controller",
        executable="serial_node",
    )

    gui_node = Node(
        package="1DOF_arm_controller",
        executable="gui_node"
    )

    # apps_node = Node(
    #     package="1DOF_arm_controller",
    #     executable="application_node"
    # )

    ld.add_action(serial_node)
    ld.add_action(gui_node)
    # ld.add_action(apps_node)

    return ld