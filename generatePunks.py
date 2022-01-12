from PIL import Image
import numpy as np
import hashlib, os, random
import probability as prob

# Keep track of punks created
punksCreated = 0
# Keep track of filehashes
fileHashes = []

# Punks
# Male = punks[0:4], Female = punks[4:8], Alien = punks[8], Ape = punks[9], Zombie = punks[10]
punks = ['punk01.png', 'punk02.png', 'punk03.png', 'punk04.png', 'punk05.png', 'punk06.png', 'punk07.png', 'punk08.png', 'punk09.png', 'punk10.png', 'punk11.png']
punkTypes = ['male', 'female', 'alien', 'ape', 'zombie']
backgrounds = ['bg01.png', 'bg02.png', 'bg03.png']
smokes = ['smoke01.png', 'smoke02.png', 'smoke03.png']

def generatePunk(punkType):
	# This can probably be shortened using dynamic variable names or similar
	if punkType == 'male':
		attrDict = prob.maleAttr
		punkStack = Image.open(f"punks/{random.choice(punks[0:4])}")
	elif punkType == 'female':
		attrDict = prob.femaleAttr
		punkStack = Image.open(f"punks/{random.choice(punks[4:8])}")
	elif punkType == 'alien':
		attrDict = prob.alienAttr
		punkStack = Image.open(f"punks/{punks[8]}")
	elif punkType == 'ape':
		attrDict = prob.apeAttr
		punkStack = Image.open(f"punks/{punks[9]}")
	elif punkType == 'zombie':
		attrDict = prob.zombieAttr
		punkStack = Image.open(f"punks/{punks[10]}")

	attributeCount = 0
	basedir = f"attributes/{punkType}/"
	hasHeadAttr = np.random.choice([True, False], p=[0.7, 0.3])
	if hasHeadAttr:
		headAttrs = [f"{basedir}head/{item[0]}" for item in attrDict['head'].items()]
		headChoice = Image.open(np.random.choice(headAttrs, p=list(attrDict['head'].values())))
		punkStack.paste(headChoice, (0, 0), headChoice)
		attributeCount += 1
	if punkType == 'male' or punkType == 'zombie':
		hasFacialHair = np.random.choice([True, False], p=[0.3, 0.7])
		if hasFacialHair:
			facialHairAttrs = [f"{basedir}facialhair/{item[0]}" for item in attrDict['facialhair'].items()]
			facialHairChoice = Image.open(np.random.choice(facialHairAttrs, p=list(attrDict['facialhair'].values())))
			punkStack.paste(facialHairChoice, (0, 0), facialHairChoice)
			attributeCount += 1
	hasGlasses = np.random.choice([True, False], p=[0.7, 0.3])
	if hasGlasses:
		glassesAttrs = [f"{basedir}eyes/{item[0]}" for item in attrDict['eyes'].items()]
		if glassesAttrs:
			glassesChoice = Image.open(np.random.choice(glassesAttrs, p=list(attrDict['eyes'].values())))
			punkStack.paste(glassesChoice, (0, 0), glassesChoice)
			attributeCount += 1
	hasMouthModifier = np.random.choice([True, False], p=[0.6, 0.4])
	if hasMouthModifier:
		mouthAttrs = [f"{basedir}mouth/{item[0]}" for item in attrDict['mouth'].items()]
		if mouthAttrs:
			mouthChoice = Image.open(np.random.choice(mouthAttrs, p=list(attrDict['mouth'].values())))
			punkStack.paste(mouthChoice, (0, 0), mouthChoice)
			attributeCount += 1
	hasMask = np.random.choice([True, False], p=[0.025, 0.975])
	if not hasMask:
		hasSmoke = np.random.choice([True, False], p=[.25, .75])
		if hasSmoke:
			smokeChoice = Image.open(f"attributes/uni/smoke/{np.random.choice(smokes, p=[0.33, 0.33, 0.34])}")
			punkStack.paste(smokeChoice, (0, 0), smokeChoice)
			attributeCount += 1
	if hasMask and punkType != 'ape':
		maskChoice = Image.open(f"{basedir}mask/mask01.png")
		punkStack.paste(maskChoice, (0, 0), maskChoice)
		attributeCount += 1
	hasEarring = np.random.choice([True, False], p=[0.15, 0.85])
	if hasEarring:
		earringChoice = Image.open(f"{basedir}earring/earring01.png")
		punkStack.paste(earringChoice, (0, 0), earringChoice)
		attributeCount += 1
	hasNecklace = np.random.choice([True, False], p=[0.2, 0.8])
	if hasNecklace:
		neckAttrs = [f"{basedir}neck/{item[0]}" for item in attrDict['neck'].items()]
		if neckAttrs:
			neckChoice = Image.open(np.random.choice(neckAttrs, p=list(attrDict['neck'].values())))
			punkStack.paste(neckChoice, (0, 0), neckChoice)
			attributeCount += 1
	if attributeCount > 6:
		print(f"Creating {punkType} with {attributeCount} attributes")
	return punkStack

# While loop for total number of punks to be generated
while punksCreated < 10000:

	# Select punk and start stacking randomly chosen layers using the appropriate function
	output = generatePunk(np.random.choice(punkTypes, p=[0.5, 0.3, 0.05, 0.06, 0.09]))

	fileHash = hashlib.md5(output.tobytes())
	hashDigest = fileHash.hexdigest()
	if hashDigest not in fileHashes:
		fileHashes.append(hashDigest)
		punkBg = Image.open(f"backgrounds/{np.random.choice(backgrounds, p=[0.7, 0.2, 0.1])}")
		punkBg.paste(output, (0, 0), output)
		punkBg.save(f"generated/FakePunk_{punksCreated}.png")
		print(f"Wrote file FakePunk_{punksCreated}.png ({hashDigest})")
		punksCreated += 1