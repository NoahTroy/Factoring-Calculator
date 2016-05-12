#Written By Noah Troy
#Define A Function To Which We Will Supply The Integers Under The Square Root Sign For Solving:
def SolveUnderSquareRoot(UnderSqrt):
	#import the math module for more advanced mathematical operators:
	import math
	'''#As to not have to regenerate the most common square roots each time the program is loaded, we have provided the first 1000,
for efficiency and convenience.'''
	listoffirst1000powers = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801, 10000, 10201, 10404, 10609, 10816, 11025, 11236, 11449, 11664, 11881, 12100, 12321, 12544, 12769, 12996, 13225, 13456, 13689, 13924, 14161, 14400, 14641, 14884, 15129, 15376, 15625, 15876, 16129, 16384, 16641, 16900, 17161, 17424, 17689, 17956, 18225, 18496, 18769, 19044, 19321, 19600, 19881, 20164, 20449, 20736, 21025, 21316, 21609, 21904, 22201, 22500, 22801, 23104, 23409, 23716, 24025, 24336, 24649, 24964, 25281, 25600, 25921, 26244, 26569, 26896, 27225, 27556, 27889, 28224, 28561, 28900, 29241, 29584, 29929, 30276, 30625, 30976, 31329, 31684, 32041, 32400, 32761, 33124, 33489, 33856, 34225, 34596, 34969, 35344, 35721, 36100, 36481, 36864, 37249, 37636, 38025, 38416, 38809, 39204, 39601, 40000, 40401, 40804, 41209, 41616, 42025, 42436, 42849, 43264, 43681, 44100, 44521, 44944, 45369, 45796, 46225, 46656, 47089, 47524, 47961, 48400, 48841, 49284, 49729, 50176, 50625, 51076, 51529, 51984, 52441, 52900, 53361, 53824, 54289, 54756, 55225, 55696, 56169, 56644, 57121, 57600, 58081, 58564, 59049, 59536, 60025, 60516, 61009, 61504, 62001, 62500, 63001, 63504, 64009, 64516, 65025, 65536, 66049, 66564, 67081, 67600, 68121, 68644, 69169, 69696, 70225, 70756, 71289, 71824, 72361, 72900, 73441, 73984, 74529, 75076, 75625, 76176, 76729, 77284, 77841, 78400, 78961, 79524, 80089, 80656, 81225, 81796, 82369, 82944, 83521, 84100, 84681, 85264, 85849, 86436, 87025, 87616, 88209, 88804, 89401, 90000, 90601, 91204, 91809, 92416, 93025, 93636, 94249, 94864, 95481, 96100, 96721, 97344, 97969, 98596, 99225, 99856, 100489, 101124, 101761, 102400, 103041, 103684, 104329, 104976, 105625, 106276, 106929, 107584, 108241, 108900, 109561, 110224, 110889, 111556, 112225, 112896, 113569, 114244, 114921, 115600, 116281, 116964, 117649, 118336, 119025, 119716, 120409, 121104, 121801, 122500, 123201, 123904, 124609, 125316, 126025, 126736, 127449, 128164, 128881, 129600, 130321, 131044, 131769, 132496, 133225, 133956, 134689, 135424, 136161, 136900, 137641, 138384, 139129, 139876, 140625, 141376, 142129, 142884, 143641, 144400, 145161, 145924, 146689, 147456, 148225, 148996, 149769, 150544, 151321, 152100, 152881, 153664, 154449, 155236, 156025, 156816, 157609, 158404, 159201, 160000, 160801, 161604, 162409, 163216, 164025, 164836, 165649, 166464, 167281, 168100, 168921, 169744, 170569, 171396, 172225, 173056, 173889, 174724, 175561, 176400, 177241, 178084, 178929, 179776, 180625, 181476, 182329, 183184, 184041, 184900, 185761, 186624, 187489, 188356, 189225, 190096, 190969, 191844, 192721, 193600, 194481, 195364, 196249, 197136, 198025, 198916, 199809, 200704, 201601, 202500, 203401, 204304, 205209, 206116, 207025, 207936, 208849, 209764, 210681, 211600, 212521, 213444, 214369, 215296, 216225, 217156, 218089, 219024, 219961, 220900, 221841, 222784, 223729, 224676, 225625, 226576, 227529, 228484, 229441, 230400, 231361, 232324, 233289, 234256, 235225, 236196, 237169, 238144, 239121, 240100, 241081, 242064, 243049, 244036, 245025, 246016, 247009, 248004, 249001, 250000, 251001, 252004, 253009, 254016, 255025, 256036, 257049, 258064, 259081, 260100, 261121, 262144, 263169, 264196, 265225, 266256, 267289, 268324, 269361, 270400, 271441, 272484, 273529, 274576, 275625, 276676, 277729, 278784, 279841, 280900, 281961, 283024, 284089, 285156, 286225, 287296, 288369, 289444, 290521, 291600, 292681, 293764, 294849, 295936, 297025, 298116, 299209, 300304, 301401, 302500, 303601, 304704, 305809, 306916, 308025, 309136, 310249, 311364, 312481, 313600, 314721, 315844, 316969, 318096, 319225, 320356, 321489, 322624, 323761, 324900, 326041, 327184, 328329, 329476, 330625, 331776, 332929, 334084, 335241, 336400, 337561, 338724, 339889, 341056, 342225, 343396, 344569, 345744, 346921, 348100, 349281, 350464, 351649, 352836, 354025, 355216, 356409, 357604, 358801, 360000, 361201, 362404, 363609, 364816, 366025, 367236, 368449, 369664, 370881, 372100, 373321, 374544, 375769, 376996, 378225, 379456, 380689, 381924, 383161, 384400, 385641, 386884, 388129, 389376, 390625, 391876, 393129, 394384, 395641, 396900, 398161, 399424, 400689, 401956, 403225, 404496, 405769, 407044, 408321, 409600, 410881, 412164, 413449, 414736, 416025, 417316, 418609, 419904, 421201, 422500, 423801, 425104, 426409, 427716, 429025, 430336, 431649, 432964, 434281, 435600, 436921, 438244, 439569, 440896, 442225, 443556, 444889, 446224, 447561, 448900, 450241, 451584, 452929, 454276, 455625, 456976, 458329, 459684, 461041, 462400, 463761, 465124, 466489, 467856, 469225, 470596, 471969, 473344, 474721, 476100, 477481, 478864, 480249, 481636, 483025, 484416, 485809, 487204, 488601, 490000, 491401, 492804, 494209, 495616, 497025, 498436, 499849, 501264, 502681, 504100, 505521, 506944, 508369, 509796, 511225, 512656, 514089, 515524, 516961, 518400, 519841, 521284, 522729, 524176, 525625, 527076, 528529, 529984, 531441, 532900, 534361, 535824, 537289, 538756, 540225, 541696, 543169, 544644, 546121, 547600, 549081, 550564, 552049, 553536, 555025, 556516, 558009, 559504, 561001, 562500, 564001, 565504, 567009, 568516, 570025, 571536, 573049, 574564, 576081, 577600, 579121, 580644, 582169, 583696, 585225, 586756, 588289, 589824, 591361, 592900, 594441, 595984, 597529, 599076, 600625, 602176, 603729, 605284, 606841, 608400, 609961, 611524, 613089, 614656, 616225, 617796, 619369, 620944, 622521, 624100, 625681, 627264, 628849, 630436, 632025, 633616, 635209, 636804, 638401, 640000, 641601, 643204, 644809, 646416, 648025, 649636, 651249, 652864, 654481, 656100, 657721, 659344, 660969, 662596, 664225, 665856, 667489, 669124, 670761, 672400, 674041, 675684, 677329, 678976, 680625, 682276, 683929, 685584, 687241, 688900, 690561, 692224, 693889, 695556, 697225, 698896, 700569, 702244, 703921, 705600, 707281, 708964, 710649, 712336, 714025, 715716, 717409, 719104, 720801, 722500, 724201, 725904, 727609, 729316, 731025, 732736, 734449, 736164, 737881, 739600, 741321, 743044, 744769, 746496, 748225, 749956, 751689, 753424, 755161, 756900, 758641, 760384, 762129, 763876, 765625, 767376, 769129, 770884, 772641, 774400, 776161, 777924, 779689, 781456, 783225, 784996, 786769, 788544, 790321, 792100, 793881, 795664, 797449, 799236, 801025, 802816, 804609, 806404, 808201, 810000, 811801, 813604, 815409, 817216, 819025, 820836, 822649, 824464, 826281, 828100, 829921, 831744, 833569, 835396, 837225, 839056, 840889, 842724, 844561, 846400, 848241, 850084, 851929, 853776, 855625, 857476, 859329, 861184, 863041, 864900, 866761, 868624, 870489, 872356, 874225, 876096, 877969, 879844, 881721, 883600, 885481, 887364, 889249, 891136, 893025, 894916, 896809, 898704, 900601, 902500, 904401, 906304, 908209, 910116, 912025, 913936, 915849, 917764, 919681, 921600, 923521, 925444, 927369, 929296, 931225, 933156, 935089, 937024, 938961, 940900, 942841, 944784, 946729, 948676, 950625, 952576, 954529, 956484, 958441, 960400, 962361, 964324, 966289, 968256, 970225, 972196, 974169, 976144, 978121, 980100, 982081, 984064, 986049, 988036, 990025, 992016, 994009, 996004, 998001, 1000000, 1002001]
	#Check to make sure that the input is an integer, to help weed out any errors later on:
	try:
		UnderSqrt = int(UnderSqrt)
	except ValueError as ErrorMessage:
		print('Error Message Geek Speak:\t' , ErrorMessage)
		print('Layman Terms: \tYou Must Enter Valid Integers')
		return
	except:
		print('An Unknown Error Occurred')
	'''#We can eliminate the upper half of the number, since it will never contain any other square roots that divide the number evenly.
This will make the code more efficient:'''
	if (UnderSqrt % 2) == 0:
		HalfOfUnderSqrt = (UnderSqrt/2)
	else:
		HalfOfUnderSqrt = ((UnderSqrt + 1) / 2)
	currentindex = 0
	quotientsthatareints = []
	#Run through all possible square roots:
	while listoffirst1000powers[currentindex] <= HalfOfUnderSqrt:
		isinteger = UnderSqrt/listoffirst1000powers[currentindex]
		if isinteger == int(isinteger):
			quotientsthatareints.append(listoffirst1000powers[currentindex])
		currentindex +=1
	#If the number can't be simplified down, just return the number back:
	if len(quotientsthatareints) == 0:
		return UnderSqrt
	else:
		finalindex = len(quotientsthatareints) - 1
		biggestdivisor = quotientsthatareints[finalindex]
		#Divide the number under the square root by an exponential number it is evenly devisable by, then find and present the square root of that number
		remainder = UnderSqrt/biggestdivisor
		isintremainder = math.sqrt(remainder)
		print('\n\n' , UnderSqrt , ' can be simplified down to:' , sep = '' , end = '\t')
		biggestdivisorsimplified = math.sqrt(biggestdivisor)
		biggestdivisorsimplified = int(biggestdivisorsimplified)
		remainder = int(remainder)
		if isintremainder == int(isintremainder):
			isintremainderbool = True
		else:
			isintremainderbool = False
		if isintremainderbool:
			if isintremainder == 1:
				print(biggestdivisorsimplified)
			else:
				print(biggestdivisorsimplified , 'and' , isintremainder)
		else:
			if remainder == 1:
				print(biggestdivisorsimplified)
			else:
				print(biggestdivisorsimplified , 'and the square root of:' , remainder)
	print('\n\n\n\nRESTARTING CALCULATOR\n')


#Extra code just used to run this code whilst testig:
number = input('Please input the number under the square root:\n')
print(SolveUnderSquareRoot(number))
