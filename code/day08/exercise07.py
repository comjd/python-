"""
    技能系统
"""


class ImpactEffect:
    """
        影响效果
    """

    def impact(self):
        pass


class DamageEffect(ImpactEffect):
    """
        伤害生命的效果
    """

    def __init__(self, value=0):
        self.value = value

    def impact(self):
        super().impact()
        print('伤害%d生命' % self.value)


class CostEffect(ImpactEffect):
    """
        消耗法力的效果
    """

    def __init__(self, value=0):
        self.value = value

    def impact(self):
        super().impact()
        print('消耗%d法力' % self.value)


class LowerDefenseEffect(ImpactEffect):
    """
        降低防御力的效果
    """

    def __init__(self, value=0, time=0):
        self.value = value
        self.time = time

    def impact(self):
        super().impact()
        print('降低%.1f防御力，持续%.1f秒' % (self.value, self.time))


class SkillBaseData:
    """
        技能的基本信息类
    """

    def __init__(self, name='', level=1):
        self.name = name
        self.level = level


class SkillDeployer:
    def __init__(self, base_data=None):
        self.__base_data = base_data  # 技能基本信息类
        self.__config_file = self.load_config_file()
        self.__effect_objects = self.create_effect_objects()

    def load_config_file(self):
        """
            将每个技能名称作为键，多个影响效果作为值，可作为配置文件存储
        :return: 返回技能名称及多个影响效果的列表
        """
        return {
            "降龙十八掌": ["DamageEffect(260)", "CostEffect(100)"],
            "六脉神剑": ["DamageEffect(100)", "LowerDefenseEffect(200,0.6)"],
        }

    def create_effect_objects(self):
        """
            根据技能名称获取每个效果的类
        :return: 返回一个技能的影响效果类（多个）
        """
        # effect_objects = []
        # for item in self.__config_file[self.__base_data.name]:
        #     effect_objects.append(eval(item))
        # return effect_objects
        return [eval(item) for item in self.__config_file[self.__base_data.name]]

    def generate_skill(self):
        """
            释放技能
        :return:
        """
        print(self.__base_data.name)
        for item in self.__effect_objects:
            item.impact()


sd = SkillDeployer(SkillBaseData('降龙十八掌', 1))
sd.generate_skill()
sd = SkillDeployer(SkillBaseData('六脉神剑', 1))
sd.generate_skill()
