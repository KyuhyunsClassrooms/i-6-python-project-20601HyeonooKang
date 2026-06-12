# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 
# 프로젝트 주제: 
class Character:
    def __init__(self, name, max_hp, skill1_name, skill1_dmg, skill1_speed, skill2_name, skill2_dmg, skill2_speed):
        # 💡 보낸 데이터들을 2차원 리스트 형태로 묶어서 저장합니다!
        self.name = name
        self.hp = max_hp
        self.max_hp = max_hp
        self.dead = 0
        self.skills = [
            [skill1_name, skill1_dmg, 0, skill1_speed],
            [skill2_name, skill2_dmg, 0, skill2_speed] 
        ]

    # 캐릭터의 정보를 보여주는 함수
    def show_info(self):
        print(f"=== [{self.name}] 상태창 ===")
        print(f"체력: {self.hp}/{self.max_hp}")
        # 2차원 리스트에서 데이터를 꺼내서 출력하기
        print(f"기술 1: {self.skills[0][0]} (데미지: {self.skills[0][1]}, 충전도: {self.skills[0][2]} / {self.skills[0][3]})")
        print(f"기술 2: {self.skills[1][0]} (데미지: {self.skills[1][1]}, 충전도: {self.skills[1][2]} / {self.skills[1][3]})")
        print("========================")

    def attack(self, skill_idx, target):
        skill_name = self.skills[skill_idx][0]
        damage = self.skills[skill_idx][1]
        
        # 1. 일단 현재 게이지(2번 열)를 1 증가시킵니다.
        self.skills[skill_idx][2] += 1  
        
        current_gauge = self.skills[skill_idx][2]
        required_speed = self.skills[skill_idx][3]
        
        # 2. 조건문 검사: 기가 다 찼는가?
        if current_gauge >= required_speed:
            # 🎉 기가 다 찼으므로 즉시 발사! (충전 중 메시지는 나오지 않음)
            self.skills[skill_idx][2] = 0  # 게이지 리셋
            
            if damage < 0:
                heal_amount = -damage
                target.hp += heal_amount
                if target.hp > target.max_hp: target.hp = target.max_hp
                print(f"✨ [시전 완료] {self.name}의 {skill_name}! {target.name}의 체력이 {heal_amount} 회복되었습니다.")
            else:
                target.hp -= damage
                if target.hp < 0: target.hp = 0
                print(f"⚔️ [시전 완료] {self.name}의 {skill_name}! {target.name}에게 {damage}의 피해!")
            return True # 기술 발사 성공
            
        else:
            # ⏳ 아직 기가 부족하여 발사되지 않을 때만 이 메시지가 출력됩니다!
            print(f"⚡ {self.name}이(가) [{skill_name}] 충전 중... (게이지: {current_gauge}/{required_speed})")
            return False # 기술 발사 실패 (대기 중)


    


def input_safe_int(prompt_message):
    while True:
        try:
            # 사용자의 입력을 받고 정수로 변환을 시도합니다.
            value = int(input(prompt_message))
            return value  # 성공하면 정수 값을 반환하고 함수를 종료합니다.
        except ValueError:
            # 만약 숫자가 아닌 문자(예: "오십", "abc")를 입력해 에러가 나면 여기로 옵니다.
            print("잘못된 입력입니다! 정수(숫자)만 입력해 주세요.")

def create_team(team_name):
    print(f"\n=== {team_name} 생성 시작 ===")
    team_list = []
    
    # 💡 int(input(...)) 대신에 우리가 만든 input_safe_int를 사용합니다!
    count = input_safe_int(f"{team_name}의 캐릭터 수는 몇 명인가요?: ")
    
    for i in range(count):
        print(f"\n[{team_name}] {i+1}번째 캐릭터 정보 입력")
        name = input("캐릭터 이름: ")
        
        # 💡 체력 입력 시 문자를 넣어도 이제 튕기지 않습니다.
        max_hp = input_safe_int("최대 체력: ")
        
        print("--- 기술 1 정보 입력 ---")
        s1_name = input("기술 1 이름: ")
        s1_dmg = input_safe_int("기술 1 데미지 (음수는 회복): ")
        s1_speed = input_safe_int("기술 1 충전 속도: ")
        
        print("--- 기술 2 정보 입력 ---")
        s2_name = input("기술 2 이름: ")
        s2_dmg = input_safe_int("기술 2 데미지 (음수는 회복): ")
        s2_speed = input_safe_int("기술 2 충전 속도: ")
        
        # Character 객체 생성 및 추가 (저번 단계 코드 적용)
        character = Character(name, max_hp, s1_name, s1_dmg, s1_speed, s2_name, s2_dmg, s2_speed)
        team_list.append(character)
        
    return team_list
  
    
def is_team_defeated(team_list):
    # 팀에 있는 모든 캐릭터를 검사합니다.
    for character in team_list:
        if character.hp > 0:
            return False  # 한 명이라도 살아있다면 전멸이 아니므로 False 반환
    return True  # 루프를 다 돌았는데도 살아있는 사람이 없다면 전멸(True) 반환



create_team('아군')
create_team('적군')

print("\n==========================================")
print("⚔️💥 대망의 전투가 시작되었습니다! 💥⚔️")
print("==========================================")

round_count = 1

# 한 팀이 완전히 전멸할 때까지 무한히 반복되는 배틀 사이클
while True:
    print(f"\n─────────────────── [ROUND {round_count}] ───────────────────")
    
    # ----------------------------------------------------
    # 😎 1. 아군(플레이어) 팀의 턴
    # ----------------------------------------------------
    print("\n🔵 >>> 아군 팀의 공격 차례입니다! <<<")
    
    for attacker in team1:
        if attacker.hp <= 0:
            continue  # 쓰러진 아군은 행동할 수 없음
            
        print(f"\n🌟 [{attacker.name}]의 행동 선택")
        
        # [스킬 고르기]
        while True:
            print(f"  [0] {attacker.skills[0][0]} (데미지:{attacker.skills[0][1]} / 게이지:{attacker.skills[0][2]}/{attacker.skills[0][3]})")
            print(f"  [1] {attacker.skills[1][0]} (데미지:{attacker.skills[1][1]} / 게이지:{attacker.skills[1][2]}/{attacker.skills[1][3]})")
            skill_idx = input_safe_int("  사용할 스킬 번호를 선택하세요 (0 또는 1): ")
            if skill_idx == 0 or skill_idx == 1:
                break
            print("  ❌ 올바른 스킬 번호를 선택해주세요.")
            
        # [딜/힐 자동 팀 타겟팅 판정]
        damage = attacker.skills[skill_idx][1]
        if damage < 0:
            target_team = team1       # 힐 마법이면 타겟은 아군 리스트
            target_team_name = "아군"
        else:
            target_team = team2       # 딜 공격이면 타겟은 적군 리스트
            target_team_name = "적군"
            
        # [구체적인 타겟 캐릭터 고르기]
        while True:
            print(f"\n  🎯 [{target_team_name}] 중에서 대상을 지정하세요.")
            for idx, member in enumerate(target_team):
                status = f"HP: {member.hp}/{member.max_hp}" if member.hp > 0 else "❌ 쓰러짐"
                print(f"  [{idx}] {member.name} ({status})")
                
            char_idx = input_safe_int("  대상의 번호를 입력하세요: ")
            
            if 0 <= char_idx < len(target_team):
                if target_team[char_idx].hp > 0:
                    target = target_team[char_idx]  # 최종 target 객체 획정!
                    break
                else:
                    print(f"  ❌ 이미 쓰러진 {target_team_name}입니다. 다시 선택하세요.")
            else:
                print(f"  ❌ 존재하지 않는 {target_team_name} 번호입니다. 다시 선택하세요.")