# encoding: utf-8

# 母港
def get_port():
	cmd = {}
	cmd['port'] = dict()
	#cmd['refill']['f1'] = ("cmd content", blur, (click x, click y))
	cmd['port']['home'] = ("司令、しっかり食べてるか？", (47, 48), 20)
	cmd['port']['go'] = ("第十七驅逐艦隊磯風，參上！", (195, 263), 20)
	cmd['port']['ok'] = ("選擇遠征", (678, 444), 3)
	cmd['port']['poi'] = ("どうした。", (623, 282), 3)
	return cmd

# 遠征
def get_expedition():
	cmd = {}
	cmd['expedition'] = dict()
	#cmd['refill']['f1'] = ("cmd content", blur, (click x, click y))
	cmd['expedition']['enter'] = ("進入遠征", (678, 224), 20)
	cmd['expedition']['e1'] = ("鎮守府海域", (136, 434), 3)
	cmd['expedition']['e2'] = ("南西諸島海域", (199, 435), 3)
	cmd['expedition']['e3'] = ("北方海域", (257, 440), 3)
	cmd['expedition']['e4'] = ("西方海域", (309, 439), 3)
	cmd['expedition']['e5'] = ("南方海域", (368, 439), 3)
	cmd['expedition']['1'] = ("1", (169, 173), 3)
	cmd['expedition']['2'] = ("2", (167, 202), 3)
	cmd['expedition']['3'] = ("3", (171, 235), 3)
	cmd['expedition']['4'] = ("4", (174, 261), 3)
	cmd['expedition']['5'] = ("5", (174, 290), 3)
	cmd['expedition']['6'] = ("5", (181, 321), 3)
	cmd['expedition']['7'] = ("7", (176, 351), 3)
	cmd['expedition']['8'] = ("8", (176, 382), 3)
	cmd['expedition']['f2'] = ("遠征隊2", (394, 117), 0)
	cmd['expedition']['f3'] = ("遠征隊3", (423, 117), 0)
	cmd['expedition']['f4'] = ("遠征隊4", (455, 117), 0)
	cmd['expedition']['ok'] = ("選擇遠征", (678, 444), 3)
	cmd['expedition']['c'] = ("取消選擇", (84, 371), 3)
	cmd['expedition']['start'] = ("出發", (629, 447), 3)
	cmd['expedition']['stop'] = ("召回", (702, 443), 3)
	cmd['expedition']['c'] = ("確定召回", (313, 290), 3)
	cmd['expedition']['c'] = ("取消召回", (489, 287), 3)
	return cmd

# 補給
def get_refill():
	cmd = {}
	cmd['refill'] = dict()
	#cmd['refill']['f1'] = ("cmd content", blur, (click x, click y))
	cmd['refill']['enter'] = ("補給は大事だ、それ無くしては戦えぬ。", (23, 208), 3)
	cmd['refill']['f1'] = ("f1", (148, 120), 3)
	cmd['refill']['f2'] = ("f2", (179, 120), 3)
	cmd['refill']['f3'] = ("f3", (207, 120), 3)
	cmd['refill']['f4'] = ("f4", (238, 120), 3)
	cmd['refill']['all'] = ("ALL", (118, 120), 3)
	cmd['refill']['1'] = ("1", (119, 166), 3)
	cmd['refill']['2'] = ("2", (119, 219), 3)
	cmd['refill']['3'] = ("3", (119, 270), 3)
	cmd['refill']['4'] = ("4", (119, 323), 3)
	cmd['refill']['5'] = ("5", (119, 373), 3)
	cmd['refill']['6'] = ("5", (119, 426), 3)
	cmd['refill']['oil'] = ("oil", (635, 442), 3)
	cmd['refill']['bullet'] = ("bullet", (768, 444), 3)
	return cmd

