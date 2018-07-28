# -*-coding:utf-8-*-
def inputs_nums():
	num_heads = int(input("input heads(m): "))
	num_feet = int(input("input feet(n): "))

	return num_heads, num_feet


def judge_inputs():
	while True:
		try:
			h, f = inputs_nums()
			return h, f
		except:
			print("Wrong Inputs！Please Enter an Integer.")


def cal_nums(h, f):
	remainder = (f - 2 * h) % 2  # 能被2除尽, 可由float转为int,且数值不会变
	if remainder == 0:
		num_cock = int((f - 2 * h) / 2)
		if num_cock >= 0 and (h-num_cock >= 0):  # 头数不可为负
			print("Cock's num：%d\nRabbits' num：%d" % (num_cock, h - num_cock))
		else:
			print("Invalid Input！")
	else:
		print("Invalid Input！")


if __name__ == "__main__":
	heads, feet = judge_inputs()
	cal_nums(heads, feet)

