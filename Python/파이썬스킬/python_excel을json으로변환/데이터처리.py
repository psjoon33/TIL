import json

with open('baseInfo.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    # json_data[202]['식품명'] = '스트링치즈'

    idx = [
        512, 510, 509, 506, 504, 503, 502, 501, 500, 495, 494, 493, 491, 490, 489, 488, 486, 484, 482, 480, 479, 478, 477, 476, 475, 474,
        469, 468, 467, 466, 464, 463, 462, 461, 460, 458, 456, 454, 453, 452, 
451, 448, 447, 446, 441, 440, 439, 436, 426, 425, 424, 423, 422, 421, 420, 419, 418, 417, 416, 415, 414, 413, 408, 407, 406, 402, 401, 400, 399, 
397, 396, 395, 394, 393, 392, 391, 390, 389, 388, 386, 385, 384, 383, 381, 379, 375, 374, 369, 368, 365, 363, 362, 361, 360, 359, 358, 357, 356, 355, 354, 353, 
351, 350, 349, 348, 347, 346, 343, 342, 341, 340, 339, 338, 337, 336, 335, 
334, 332, 331, 330, 322, 321, 320, 317, 312, 310, 309, 308, 307, 304, 301, 296, 295, 294, 293, 290, 
289, 287, 283, 278, 277, 276, 275, 274, 273, 272, 271, 268, 267, 266, 265
    ]  
    for i in idx:
        json_data.pop(i)

    # json_data[114]['분류'] = '가공유'
    # json_data[115]['분류'] = '가공유'



with open('baseInfo.json', 'w', encoding='utf-8') as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")

