import requests, json, os, time, random, base64
BEARER_TOKEN = "Bearer ya29.a0Aa7MYioq45sCEtK68OaxC0rLfcDG123D47l4SghCS1TPF8yVpABb1K-CVgbXyu5PQE7_a8sJWEySZOAkcNmO8MFy3l6KAvsNpidyQ6fbvMZxmmDnW_DqKyhK6uay1J9JzNWn56Sihy9Pgg-KSBKWnvViI0WV9OVTCqZIfQtOyWajh3GaET-09848DY3PQy-YeQmov212vT67wKlVLlXxWjdanbTf6lT0idYdMb8L2LQSLXrriLjM3f6xxkjCAJdJfNjz9hKCq7CtSAcTZT0H-ged-1_A-8BcfuP6aRquKGfrJ1KOTZg3hf_VMAe9bbDG-UJ5LJx8MLt4UpWc90t7Yq7Ve-aCRh1OuJCMkpDjtJYeaCgYKAXQSARMSFQHGX2Mikg-80OGD6BbIeDAIDrupgw0371"
WORKFLOW_ID = "b0c9d4bc-1543-4556-b427-8804028339ea"
SUBJECT_ID = "CAMaJGIwYzlkNGJjLTE1NDMtNDU1Ni1iNDI3LTg4MDQwMjgzMzllYSIDQ0JBKiQ1ZWMwNjBmMy03ZDk2LTRhNmEtYTM4ZC05YTJhNDFjNGQyMTY"
SUBJECT_CAPTION = "Amara 19 ans jeune artiste West African woman natural short hair paint stains warm golden tones"
STYLE_ID = "CAMaJGIwYzlkNGJjLTE1NDMtNDU1Ni1iNDI3LTg4MDQwMjgzMzllYSIDQ0FFKiRjMzBhY2UyNy03YTNhLTQ4NWUtOGNjMS1mOWZiNGU1YzM2N2Y"
STYLE_CAPTION = "Illustration digitale semi-realiste style animation cinematographique moderne"
ASPECT_RATIO = "IMAGE_ASPECT_RATIO_LANDSCAPE"
OUTPUT_DIR = os.path.expanduser("~/storage/downloads/whisk_projet2")
API_URL = "https://aisandbox-pa.googleapis.com/v1/whisk:runImageRecipe"
HEADERS = {"Authorization": BEARER_TOKEN, "Content-Type": "application/json"}
DELAY_MIN = 8
DELAY_MAX = 15
START_FROM = 51
PROMPTS = [
"Wide aerial establishing shot of a prosperous West African urban neighborhood at golden hour tree-lined streets walled compounds colorful markets",
"Detailed street-level view of a wealthy West African home entrance massive ornate golden metal gate white stone driveway perfectly manicured lawn",
"A grand West African colonial-style house gleaming under bright sunlight whitewashed walls radiating prosperity lush garden tall iron gate",
"Night exterior of a wealthy West African house warm lights glowing from upper windows tiny silhouette of a child visible through curtain",
"Simple bold title card the name AMARA written in warm hand-drawn letters on aged paper with a single small flower soft warm light",
"Full body portrait of a 9-year-old West African girl in worn school clothes short rough hair small hands marked by work plain wall",
"Symbolic image a single small girl silhouette standing alone under a vast open African sky isolated posture and empty space around her",
"A 6-year-old West African girl sitting beside her ill mother bed her tiny hands gripping the edge confused and frightened but brave",
"Sensory memory image soft soap bubbles dissolving over wet dark earth warm amber light delicate water droplets adult dark arms barely visible",
"A young West African man in his late 20s walking away down a dusty narrow city street his back to the camera not looking back",
"A young West African woman alone in a small rented room a baby girl on a mat beside her quiet determination despite exhaustion",
"Pre-dawn street scene a young West African woman setting up a beignet stall in darkness oil lamp just beginning to illuminate her work",
"Afternoon scene a young West African woman on her knees scrubbing laundry in a shared courtyard dignified survival harsh midday light",
"Evening scene a young West African woman returning home exhausted her small daughter running to meet her tired smile warm dusk light",
"Abstract visual metaphor a fast-moving illness represented as dark smoke rushing across a warm amber background engulfing a gentle female silhouette",
"Street scene a tall imposing well-dressed woman arriving at a modest housing compound taking the hand of a small confused girl neighbors watching",
"Close-up of expensive gold earrings against a West African woman dark skin her head held high costly pagne catching the light",
"Public scene Tante Adjoa standing in a compound courtyard holding little Amara hand speaking to gathered neighbors with performed generosity",
"The heavy wooden front door of a wealthy West African home swinging shut with finality the neighborhood visible shrinking through the closing gap",
"Kitchen scene in a wealthy West African home a small girl washing a large pile of dishes her arms barely reaching soap suds on face",
"A small girl heating water in a large pot on a wood stove carefully not to burn herself the early morning light just beginning",
"A small girl eating standing in a kitchen corner leftovers from others meals around her eyes downcast photorealistic melancholic realism",
"Close-up of a girl hand reaching for the very last piece of bread on a kitchen counter emptiness of her portion warm kitchen light",
"A modest West African primary school exterior at morning children in blue and white uniforms filing through the gate bright morning light",
"A West African primary school teacher pointing to the board students listening in far back corner a small girl sitting very still barely noticed",
"A university or art school memory scene a younger version of Mr Mensah in a bright studio surrounded by canvases paint on his hands",
"Close-up of Mr Mensah face as he looks at children drawings his expression showing deep private conviction warm classroom light shallow depth of field",
"Children drawings spread across wooden school desks houses with yellow suns smiling dogs families at tables trees innocent colorful artwork",
"Child artwork close-up two crossed hands floating in empty space warm yellow-orange light glowing at center dense dark night surrounding them",
"Mr Mensah leaning down to a girl desk level asking gently if the drawing is her own work his body language non-threatening and kind",
"A girl shaking her head slowly in confirmation expression caught between wariness and wonder at an adult speaking with gentleness",
"Before and after split image left a girl with downcast eyes right the same girl with eyes slightly lifted the moment two words changed everything",
"After-school scene Mr Mensah sitting at his desk writing notes about a student a child drawing lying beside his papers afternoon light",
"Close-up of a child hands receiving a stack of blank white sheets from a teacher the paper bright and full of possibility warm light",
"A stack of art books open on a school desk showing African paintings sculptures a small girl hands turning pages with reverence and wonder",
"Close-up portrait series African women faces painted with complex micro-emotions grief beneath a smile pride beneath exhaustion love beneath fear",
"Vibrant birds-eye view painting of a West African open-air market explosion of colors fabric stalls pyramids of spices women balancing basins",
"A child drawing of market sounds made visual bold curving lines suggesting noise bursts of color for smells movement lines for bodies of traders",
"A child pencil sketch of children running barefoot through dusty red earth their laughter implied by open mouths and windswept movements",
"A child drawing of elderly men seated in the shade of a large mango tree their postures showing calm wisdom detailed wrinkles in pencil",
"A child painting of women carrying large clay jars on their heads their spines perfectly straight walking in line with effortless grace royalty",
"A series of hand drawings evolving across multiple sheets open hands receiving closed fists resisting cupped hands protecting a flame",
"Close-up of a child drawing of two gentle careful hands made with obvious love and memory the hands of a mother remembered through art",
"A wealthy West African home living room two girls in expensive clothes with school friends while another girl quietly carries a heavy tray",
"A small girl setting down a silver tray on a coffee table surrounded by well-dressed older girls laughing her eyes immediately cast to floor",
"A small girl walking back toward the kitchen her figure diminishing in the hallway while laughter continues in the bright social room behind her",
"A West African woman standing in her living room elegant posture her expression showing displeasure harsh overhead light gold jewelry",
"A small West African girl looking thoughtfully into the distance her face showing quiet inner strength warm afternoon light",
"Abstract symbolic image a small glowing flame burning steadily inside a dark storm metaphor for prayer and creative survival warm persistent",
"Mr Mensah holding a child drawing made on the back of flattened cardboard turning it carefully his expression shifting to deep concern warm light",
]
def find_b64(obj, results):
 if isinstance(obj, dict):
  for k, v in obj.items():
   if k in ['encodedImage','imageBytes','data','image'] and isinstance(v, str) and len(v) > 200:
    results.append(v)
   else:
    find_b64(v, results)
 elif isinstance(obj, list):
  for item in obj:
   find_b64(item, results)
def save_images(data, index):
 saved = 0
 b64_list = []
 find_b64(data, b64_list)
 for i, b64 in enumerate(b64_list):
  try:
   path = f"{OUTPUT_DIR}/image_{index:04d}_{i+1}.jpg"
   with open(path, 'wb') as f:
    f.write(base64.b64decode(b64))
   print(f"  Sauvegarde: image_{index:04d}_{i+1}.jpg")
   saved += 1
  except Exception as e:
   print(f"  Erreur: {e}")
 return saved
def run():
 os.makedirs(OUTPUT_DIR, exist_ok=True)
 print(f"\n=== WHISK PROJET 2 - {len(PROMPTS)} prompts - debut image {START_FROM} ===\n")
 success = 0
 for i, prompt in enumerate(PROMPTS):
  index = i + START_FROM
  print(f"[{index}] {prompt[:60]}...")
  payload = {"clientContext": {"workflowId": WORKFLOW_ID, "tool": "BACKBONE", "sessionId": str(int(time.time()*1000))}, "seed": random.randint(100000, 999999), "imageModelSettings": {"imageModel": "GEM_PIX", "aspectRatio": ASPECT_RATIO}, "userInstruction": prompt, "recipeMediaInputs": [{"caption": SUBJECT_CAPTION, "mediaInput": {"mediaCategory": "MEDIA_CATEGORY_SUBJECT", "mediaGenerationId": SUBJECT_ID}}, {"caption": STYLE_CAPTION, "mediaInput": {"mediaCategory": "MEDIA_CATEGORY_STYLE", "mediaGenerationId": STYLE_ID}}]}
  try:
   r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
   if r.status_code == 200:
    imgs = save_images(r.json(), index)
    if imgs == 0:
     with open(f"{OUTPUT_DIR}/debug_{index:04d}.json", "w") as f:
      json.dump(r.json(), f)
     print("  OK debug JSON sauvegarde")
    success += 1
   elif r.status_code == 401:
    print("  Token expire!")
    break
   elif r.status_code == 429:
    print("  Rate limit pause 60s...")
    time.sleep(60)
   else:
    print(f"  Erreur {r.status_code}")
  except Exception as e:
   print(f"  Erreur: {e}")
  if i < len(PROMPTS) - 1:
   d = random.randint(DELAY_MIN, DELAY_MAX)
   print(f"  Pause {d}s...")
   time.sleep(d)
 print(f"\n=== TERMINE - {success}/{len(PROMPTS)} reussis ===")
run()
