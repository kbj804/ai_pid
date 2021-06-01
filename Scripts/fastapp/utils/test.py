import asyncio

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
# I am C. I slept for 3 seconds.