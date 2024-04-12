from setuptools import find_packages, setup

package_name = '1DOF_arm_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rosbot',
    maintainer_email='rosbot@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'serial_node = 1DOF_arm_controller.serial_node:main',
            'application_node = 1DOF_arm_controller.apps_node:main',
            'gui_node = 1DOF_arm_controller.gui_node:main',
            'test_node = 1DOF_arm_controller.test_node:main',
        ],
    },
)
