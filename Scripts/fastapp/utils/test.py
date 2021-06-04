def solution(clothes):
    # num = len(clothes)
    clo_dict ={}
    count = 0
    for arr in clothes:
        if arr[1] in clo_dict:
            clo_dict[arr[1]] += 1
        else:
            clo_dict[arr[1]] = 1
        count += 1
    answer = count + count -1 
    print(answer)
    return answer

solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])

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