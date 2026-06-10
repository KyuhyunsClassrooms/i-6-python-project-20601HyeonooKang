# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 
# 프로젝트 주제: 
class Character:
    def __init__(self, name, max_hp, skill1_name, skill1_dmg, skill1_speed, skill2_name, skill2_dmg, skill2_speed):
        # 💡 보낸 데이터들을 2차원 리스트 형태로 묶어서 저장합니다!
        self.skills = [
            [name,max_hp,max_hp],
            [skill1_name, skill1_dmg, skill1_speed],
            [skill2_name, skill2_dmg, skill2_speed] 
        ]

    # 캐릭터의 정보를 보여주는 함수
    def show_info(self):
        print(f"=== [{self.skills[0][0]}] 상태창 ===")
        print(f"체력: {self.skills[0][1]}/{self.skills[0][2]}")
        # 2차원 리스트에서 데이터를 꺼내서 출력하기
        print(f"기술 1: {self.skills[1][0]} (데미지: {self.skills[1][1]}, 속도: {self.skills[1][2]})")
        print(f"기술 2: {self.skills[2][0]} (데미지: {self.skills[2][1]}, 속도: {self.skills[2][2]})")
        print("========================")

    def attack(self, skill_idx, target):
        # skill_idx에는 1(공격1) 또는 2(공격2)이 들어옵니다.
        # 2차원 리스트(self.skills)에서 스킬 이름과 데미지를 꺼내보세요.
        skill_name = self.skills[skill_idx][0]
        damage = self.skills[skill_idx][1]
        speed = self.skills[skill_idx][2]

