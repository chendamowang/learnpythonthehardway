def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None


def scan(sentence):


    lexicon = {
	    'north': ('direction', 'north'),
	    'south': ('direction', 'south'),
	    'east': ('direction', 'east'),
	    'west': ('direction', 'west'),
	
	    'go': ('verb', 'go'),
	    'kill': ('verb', 'kill'),
	    'eat': ('verb', 'eat'),
	
	    'the': ('stop', 'the'),
	    'in': ('stop', 'in'),
	    'of': ('stop', 'of'),
	
	    'bear': ('noun', 'bear'),
	    'princess': ('noun', 'princess'),
    }
    
    words = sentence.split()
    result =  []
    for s in words:
        if convert_numbers(s):
            result.append(('number', int(s)))
        elif convert_numbers(s) == None and s in lexicon.keys():
            result.append(lexicon[s])
        else:
            result.append(('error', s))
    
    return result
