# Topologia do trabalho
T = {
        'h1': { 's1':1 },
        'h2': { 's2':1 },
        'h3': { 's3':1 },
        'h4': { 's4':1 },
        'h5': { 's5':1 },
        'h6': { 's6':1 },
        'h7': { 's7':1 },
        's1': { 'h1':1 , 's2':1 , 's8':1 , 's7':1 , 's10':1 },
        's2': { 'h2':1 , 's1':1 , 's10':1 , 's3':1  },
        's3': { 'h3':1 , 's2':1 , 's9':1 , 's4':1  },
        's4': { 'h4':1 , 's3':1 , 's5':1 , 's8':1  },
        's5': { 'h5':1 , 's4':1 , 's6':1 , 's7':1 },
        's6': { 'h6':1 , 's7':1 , 's7':1 },
        's7': { 'h7':1 , 's1':1 , 's5':1 , 's7':1 , 's8':1 },
        's8': { 's1':1 , 's4':1 , 's7':1 , 's9':1 , 's10':1 },
        's9': { 's3':1 , 's8':1 , 's10':1 },
        's10': { 's1':1 , 's2':1 , 's8':1 , 's9':1 }
    }

hosts = {'h1','h2','h3','h4','h5','h6','h7'}
switches = {'s1','s2','s3','s4','s5','s6','s7','s8','s9','s10'}
P = {
		'h1': [('s1',1)],
        'h2': [('s2',1)],
        'h3': [('s3',1)],
        'h4': [('s4',1)],
        'h5': [('s5',1)],
        'h6': [('s6',1)],
        'h7': [('s7',1)],
        's1': [('h1',1) , ('s2',2) , ('s8',3) , ('s7',4) , ('s10',5)],
        's2': [('h2',1) , ('s1',2) , ('s10',3) , ('s3',4)],
        's3': [('h3',1) , ('s2',2) , ('s9',3) , ('s4',4)],
        's4': [('h4',1) , ('s3',2) , ('s5',3) , ('s8',4)],
        's5': [('h5',1) , ('s4',2) , ('s6',3) , ('s7',4)],
        's6': [('h6',1) , ('s7',2) , ('s7',3)],
        's7': [('h7',1) , ('s1',2) , ('s5',3) , ('s7',4) , ('s8',5)],
        's8': [('s1',1) , ('s4',2) , ('s7',3) , ('s9',4) , ('s10',5)],
        's9': [('s3',1) , ('s8',2) , ('s10',3)],
        's10': [ ('s1',1) , ('s2',2) , ('s8',3) , ('s9',4)]
	}

MAC = {
		'h1': '00:04:00:00:00:01',
		'h2': '00:04:00:00:00:02',
		'h3': '00:04:00:00:00:03',
		'h4': '00:04:00:00:00:04',
		'h5': '00:04:00:00:00:05',
		'h6': '00:04:00:00:00:06',
		'h7': '00:04:00:00:00:07',
	}