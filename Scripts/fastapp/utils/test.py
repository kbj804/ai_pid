# text = ["홍길동","일지매","유관순"]

# print(f"현재 이 과목 수강 신청자는 {text} 입니다. ")

# a= input("변경 전 이름을 입력하세요 : ")
# b= input("변경 후 이름을 입력하세요 : ")

# text[text.index(a)] = b

# print(f"요청하신대로 {a} 을(를) {b} (으)로 변경하였습니다. ")
# print(f"현재 이 과목 최종 수강 신청자는 {text} 입니다. ")



"""import asyncio

async def whoami_after_sleep(name, t):
  print(f'I am {name} and gonna sleep for {t} seconds.')
  await asyncio.sleep(t)
  print(f'I am {name}. I slept for {t} seconds.')
  return ('result', name, t)

async def main():
  await asyncio.gather(
    whoami_after_sleep('A', 1),
  )
  return "ok"

print(asyncio.run(main()))

# I am A and gonna sleep for 1 seconds.
# I am B and gonna sleep for 2 seconds.
# I am C and gonna sleep for 3 seconds.
# I am A. I slept for 1 seconds.
# I am B. I slept for 2 seconds.
# I am C. I slept for 3 seconds."""