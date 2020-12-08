# Transforming mathematical angle to robot angle (robot's 0 degrees is equal to mathematical 90 degrees)
def transform_robot_angle(angles):
    angles_ret = []
    for i in range(0, len(angles)):
        robot_angle = angles[i] - 90
        if robot_angle < 0:
            robot_angle = robot_angle + 360

        robot_angle = (robot_angle * -1) + 360

        # Used SDK doesn't support setting angle to 360, must be 0
        if robot_angle == 360:
            robot_angle = 0

        angles_ret.append(robot_angle)

    return angles_ret
