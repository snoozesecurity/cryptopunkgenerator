from PIL import Image
import numpy as np
import hashlib, random

# Keep track of punks created
punksCreated = 0
# Keep track of filehashes
fileHashes = []

# Punks
# Male = punks[0:4], Female = punks[4:8], Alien = punks[8], Ape = punks[9], Zombie = punks[10]
punks = ['punk01.png', 'punk02.png', 'punk03.png', 'punk04.png', 'punk05.png', 'punk06.png', 'punk07.png', 'punk08.png', 'punk09.png', 'punk10.png', 'punk11.png']
punkTypes = ['male', 'female', 'alien', 'ape', 'zombie']

# Male attributes
head = ['hair01.png', 'hair02.png', 'hair03.png', 'hat01.png', 'hoodie.png']
glasses = ['glasses01.png', 'glasses02.png', 'glasses03.png', 'glasses04.png']
facialHair = ['beard01.png', 'beard02.png']
mask = 'mask01.png'

# Female attributes
femaleHead = ['femalehair01.png', 'femalehair02.png', 'femalehair03.png', 'femalehair04.png', 'femalehair05.png', 'femalehair06.png', 'femalehair07.png', 'femaletiara01.png', 'femalehat01.png']
femaleEyewear = ['femaleglasses01.png', 'femaleglasses02.png', 'femaleglasses03.png', 'femaleshadow01.png', 'femaleshadow02.png']
femaleMask = 'femalemask01.png'

# Ape attributes
apeHead = ['hat01.png', 'hat02.png', 'hat03.png', 'hat04.png', 'hoodie.png', 'headband01.png']
apeGlasses = ['glasses01.png', 'glasses02.png', 'glasses03.png', 'glass04.png']

# Universal attributes
backgrounds = ['bg01.png', 'bg02.png', 'bg03.png']
smokes = ['smoke01.png', 'smoke02.png', 'smoke03.png']
other = ['earring01.png']

def generateMale():
	punkStack = Image.open(f"punks/{random.choice(punks[0:4])}")
	hasHeadAttr = np.random.choice([True, False], p=[0.7, 0.3])
	if hasHeadAttr:
		headChoice = Image.open(f"attributes/{np.random.choice(head, p=[0.4, 0.15, 0.2, 0.15, 0.1])}")
		punkStack.paste(headChoice, (0, 0), headChoice)
	hasGlasses = np.random.choice([True, False], p=[0.7, 0.3])
	if hasGlasses:
		glassesChoice = Image.open(f"attributes/{np.random.choice(glasses, p=[0.4, 0.4, 0.1, 0.1])}")
		punkStack.paste(glassesChoice, (0, 0), glassesChoice)
	hasFacialHair = np.random.choice([True, False], p=[0.25, 0.75])
	if hasFacialHair:
		facialHairChoice = Image.open(f"attributes/{np.random.choice(facialHair, p=[0.5, 0.5])}")
		punkStack.paste(facialHairChoice, (0, 0), facialHairChoice)
	hasSmoke = np.random.choice([True, False], p=[0.15, 0.85])
	if hasSmoke:
		smokeChoice = Image.open(f"attributes/{np.random.choice(smokes, p=[0.3, 0.3, 0.4])}")
		punkStack.paste(smokeChoice, (0, 0), smokeChoice)
	hasMask = np.random.choice([True, False], p=[0.02, 0.98])
	if hasMask:
		maleMask = Image.open(f"attributes/{mask}")
		punkStack.paste(maleMask, (0, 0), maleMask)
	elif not hasMask:
		hasSmoke = np.random.choice([True, False], p=[0.35, 0.65])
		if hasSmoke:
			smokeChoice = Image.open(f"attributes/{np.random.choice(smokes, p=[0.3, 0.3, 0.4])}")
			punkStack.paste(smokeChoice, (0,0), smokeChoice)
	return punkStack

def generateFemale():
	punkStack = Image.open(f"punks/{random.choice(punks[4:8])}")
	hasHeadAttr = np.random.choice([True, False], p=[0.8, 0.2])
	if hasHeadAttr:
		headChoice = Image.open(f"attributes/{np.random.choice(femaleHead, p=[0.15, 0.15, 0.15, 0.15, 0.15, 0.075, 0.075, 0.025, 0.075])}")
		punkStack.paste(headChoice, (0, 0), headChoice)
	hasEyewear = np.random.choice([True, False], p=[0.8, 0.2])
	if hasEyewear:
		eyewearChoice = Image.open(f"attributes/{np.random.choice(femaleEyewear, p=[0.2, 0.2, 0.2, 0.2, 0.2])}")
		punkStack.paste(eyewearChoice, (0, 0), eyewearChoice)
	hasMask = np.random.choice([True, False], p=[0.02, 0.98])
	if hasMask:
		fMask = Image.open(f"attributes/{femaleMask}")
		punkStack.paste(fMask, (0, 0), fMask)
	elif not hasMask:
		hasSmoke = np.random.choice([True, False], p=[0.35, 0.65])
		if hasSmoke:
			smokeChoice = Image.open(f"attributes/{np.random.choice(smokes, p=[0.3, 0.3, 0.4])}")
			punkStack.paste(smokeChoice, (0,0), smokeChoice)
	return punkStack

def generateAlien():
	punkStack = Image.open(f"punks/{punks[8]}")
	hasHeadAttr = np.random.choice([True, False], p=[0.9, 0.1])
	if hasHeadAttr:
		headChoice = Image.open(f"attributes/{np.random.choice(head, p=[0.4, 0.15, 0.2, 0.15, 0.1])}")
		punkStack.paste(headChoice, (0, 0), headChoice)
	hasGlasses = np.random.choice([True, False], p=[0.7, 0.3])
	if hasGlasses:
		glassesChoice = Image.open(f"attributes/{np.random.choice(glasses, p=[0.4, 0.4, 0.1, 0.1])}")
		punkStack.paste(glassesChoice, (0, 0), glassesChoice)
	hasMask = np.random.choice([True, False], p=[0.02, 0.98])
	if hasMask:
			maleMask = Image.open(f"attributes/{mask}")
			punkStack.paste(maleMask, (0, 0), maleMask)
	elif not hasMask:
		hasSmoke = np.random.choice([True, False], p=[0.35, 0.65])
		if hasSmoke:
			smokeChoice = Image.open(f"attributes/{np.random.choice(smokes, p=[0.3, 0.3, 0.4])}")
			punkStack.paste(smokeChoice, (0,0), smokeChoice)
	return punkStack

def generateApe():
	punkStack = Image.open(f"punks/{punks[9]}")
	headChoice = Image.open(f"attributes/{np.random.choice(apeHead, p=[0.3, 0.1, 0.15, 0.2, 0.15, 0.1])}")
	punkStack.paste(headChoice, (0, 0), headChoice)
	hasGlasses = np.random.choice([True, False], p=[0.7, 0.3])
	if hasGlasses:
		glassesChoice = Image.open(f"attributes/{np.random.choice(glasses, p=[0.35, 0.35, 0.15, 0.15])}")
		punkStack.paste(glassesChoice, (0, 0), glassesChoice)
	hasSmoke = np.random.choice([True, False], p=[0.15, 0.85])
	if hasSmoke:
		smokeChoice = Image.open(f"attributes/{np.random.choice(smokes, p=[0.3, 0.3, 0.4])}")
		punkStack.paste(smokeChoice, (0,0), smokeChoice)
	return punkStack

def generateZombie():
	punkStack = Image.open(f"punks/{punks[10]}")
	hasHeadAttr = np.random.choice([True, False], p=[0.5, 0.5])
	if hasHeadAttr:
		headChoice = Image.open(f"attributes/{np.random.choice(head, p=[0.4, 0.15, 0.2, 0.15, 0.1])}")
		punkStack.paste(headChoice, (0, 0), headChoice)
	hasGlasses = np.random.choice([True, False], p=[0.7, 0.3])
	if hasGlasses:
		glassesChoice = Image.open(f"attributes/{np.random.choice(glasses, p=[0.25, 0.25, 0.25, 0.25])}")
		punkStack.paste(glassesChoice, (0, 0), glassesChoice)
	hasFacialHair = np.random.choice([True, False], p=[0.25, 0.75])
	if hasFacialHair:
		facialHairChoice = Image.open(f"attributes/{np.random.choice(facialHair, p=[0.5, 0.5])}")
		punkStack.paste(facialHairChoice, (0, 0), facialHairChoice)
	hasMask = np.random.choice([True, False], p=[0.02, 0.98])
	if hasMask:
		maleMask = Image.open(f"attributes/{mask}")
		punkStack.paste(maleMask, (0, 0), maleMask)
	return punkStack

# While loop for total number of punks to be generated
while punksCreated < 100:

	# Select punk and start stacking randomly chosen layers using the appropriate function
	punkType = np.random.choice(punkTypes, p=[0.5, 0.3, 0.05, 0.06, 0.09])

	# Function call depending on punkType
	if punkType == 'male':
		output = generateMale()
	elif punkType == 'female':
		output = generateFemale()
	elif punkType == 'alien':
		output = generateAlien()
	elif punkType == 'ape':
		output = generateApe()
	elif punkType == 'zombie':
		output = generateZombie()

	fileHash = hashlib.md5(output.tobytes())
	hashDigest = fileHash.hexdigest()
	if hashDigest not in fileHashes:
		fileHashes.append(hashDigest)
		punkBg = Image.open(f"backgrounds/{np.random.choice(backgrounds, p=[0.7, 0.2, 0.1])}")
		punkBg.paste(output, (0, 0), output)
		punkBg.save(f"generated/FakePunk_{punksCreated}.png")
		print(f"Wrote file FakePunk_{punksCreated}.png ({hashDigest})")
		punksCreated += 1