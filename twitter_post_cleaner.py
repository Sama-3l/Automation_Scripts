import keyboard, mouse, time

time.sleep(3)
for i in range(50):
    time.sleep(1)
    if i % 10 == 0:
        mouse.wheel(-0.1)
    mouse.move(971, 143)
    mouse.click()
    time.sleep(0.2)
    mouse.move(762, 156)
    mouse.click()
    time.sleep(0.3)
    mouse.move(774, 507)
    mouse.click()

print(mouse.get_position())