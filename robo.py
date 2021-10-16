import wpilib 
import wpilib.drive
import ctre

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        # os 4 motores da tração
        self.m_left_front = ctre.WPI_VictorSPX(22)
        self.m_right_front = ctre.WPI_VictorSPX(33)
        self.m_left_rear = ctre.WPI_VictorSPX(11)
        self.m_right_rear = ctre.WPI_VictorSPX(44)
        # motores dos mecanismos
        self.shooter = ctre.WPI_VictorSPX(9)
        self.track_ball = ctre.WPI_VictorSPX(8)
        self.ball_catcher = ctre.WPI_VictorSPX(55)
        # lado esquerdo e lado direito da tração
        self.m_left = wpilib.SpeedControllerGroup(self.m_left_front,self.m_left_rear)
        self.m_right = wpilib.SpeedControllerGroup(self.m_right_front,self.m_right_rear)
        # criando a traçao como um objeto
        self.myRobot = wpilib.drive.DifferentialDrive(self.m_left,self.m_right)
        self.myRobot.setExpiration(0.1)
        #criando um joystick
        self.stick = wpilib.Joystick(0)
        # criar uma camera
        wpilib.CameraServer.launch('vision.py:main')
        #criando um relogio para contar o tempo
        self.timer = wpilib.Timer()
#criando o teleoperado
def teleopInit(self):
    self.myRobot.setSafetyEnabled(True)

#criar o periodo teleoperado
def teleopPeriodic(self):
    if self.stick.getRawButton(5)   == True:
        self.myRobot.arcadeDrive(
            -self.stick.getRawAxis(1),self.stick.getRawAxis(0)*1.15,True
        )
    else:
        self.myRobot.arcadeDrive(
            self.stick.getRawAxis(1),self.stick.getRawAxis(0)*1.15,True
        )