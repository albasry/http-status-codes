http_codes = {
    'Informational responses': {
        100: 'Continue',
        101: 'Switching Protocols',
        102: 'Processing',
        103: 'Early Hints'
    },
    # 104-199 Unassigned
    'Successful responses': {
        200: 'Ok',
        201: 'Created',
        202: 'Accepted',
        203: 'Non-Authoritative Information',
        204: 'No Content',
        205: 'Reset Content',
        206: 'Partial Content',
        207: 'Multi-Status',
        208: 'Already Reported',
        226: 'IM Used'
    },
    # 209-225 Unassigned
    # 227-299 Unassigned
    'Redirection messages': {
        300: 'Multiple Choices',
        301: 'Moved Permanently',
        302: 'Found',
        303: 'See Other',
        304: 'Not Modified',
        305: 'Use Proxy',
        306: '(Unused)',
        307: 'Temporary Redirect',
        308: 'Permanent Redirect'
    },
    # 309-399 Unassigned
    'Client error responses': {
        400: 'Bad Request',
        401: 'Unauthorized',
        402: 'Payment Required',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        406: 'Not Acceptable',
        407: 'Proxy Authentication Required',
        408: 'Request Timeout',
        409: 'Conflict',
        410: 'Gone',
        411: 'Length Required',
        412: 'Precondition Failed',
        413: 'Content Too Large',
        414: 'URI Too Long',
        415: 'Unsupported Media Type',
        416: 'Range Not Satisfiable',
        417: 'Expectation Failed',
        418: '(Unused)',
        421: 'Misdirected Request',
        422: 'Unprocessable Content',
        423: 'Locked',
        424: 'Failed Dependency',
        425: 'Too Early',
        426: 'Upgrade Required',
        428: 'Precondition Required',
        429: 'Too Many Requests',
        431: 'Request Header Fields Too Large',
        451: 'Unavailable For Legal Reasons'
    },
    # 419-420 Unassigned
    # 427     Unassigned
    # 430     Unassigned
    # 432-450 Unassigned
    # 452-499 Unassigned
    'Server error responses': {
        500: 'Internal Server Error',
        501: 'Not Implemented',
        502: 'Bad Gateway',
        503: 'Service Unavailable',
        504: 'Gateway Timeout',
        505: 'HTTP Version Not Supported',
        506: 'Variant Also Negotiates',
        507: 'Insufficient Storage',
        508: 'Loop Detected',
        510: 'Not Extended (OBSOLETED)',
        511: 'Network Authentication Required'
    }
    # 509   Unassigned
    # 512-599 Unassigned
}

enter = int(input('Enter the HTTP Code: '))
response_type = list(http_codes)
if 100 <= enter <= 199:
    print(f'\n== Response Type: {response_type[0]} ==')
    if 104 <= enter <= 199:
        print('== HTTP status Code: Unassigned !! ==')
    else:
        print(f'== HTTP status Code: {http_codes["Informational responses"][enter]} ==')
elif 200 <= enter <= 299:
    print(f'\n== Response Type: {response_type[1]} ==')
    if 209 <= enter <= 225:
        print('== HTTP status Code: Unassigned !! ==')
    elif 227 <= enter <= 299:
        print('== HTTP status Code: Unassigned !! ==')
    else:
        print(f'== HTTP status Code: {http_codes["Successful responses"][enter]} ==')
elif 300 <= enter <= 399:
    print(f'\n== Response Type: {response_type[2]} ==')
    if 309 <= enter <= 399:
        print('== HTTP status Code: Unassigned !! ==')
    else:
        print(f'== HTTP status Code: {http_codes["Redirection messages"][enter]} ==')
elif 400 <= enter <= 499:
    print(f'\n== Response Type: {response_type[3]} ==')
    if enter in [419, 420, 427, 430]:
        print('== HTTP status Code: Unassigned !! ==')
    elif 432 <= enter <= 450:
        print('== HTTP status Code: Unassigned !! ==')
    elif 452 <= enter <= 499:
        print('== HTTP status Code: Unassigned !! ==')
    else:
        print(f'== HTTP status Code: {http_codes["Client error responses"][enter]} ==')
elif 500 <= enter <= 599:
    print(f'\n== Response Type: {response_type[4]} ==')
    if enter == 509:
        print('== HTTP status Code: Unassigned !! ==')
    elif 512 <= enter <= 599:
        print('== HTTP status Code: Unassigned !! ==')
    else:
        print(f'== HTTP status Code: {http_codes["Server error responses"][enter]} ==')
else:
    print('== Invalid HTTP status code ! ==')
