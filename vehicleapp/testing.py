import pandas as pd
import os
import math
import collections
import joblib
import re
from sklearn.neural_network import MLPClassifier

sql_regex = re.compile("(?P<UNION>UNION\s+(ALL\s+)?SELECT)|(?P<PREFIX>([\'\"\)]|((\'|\"|\)|\d+|\w+)\s))(\|\|\&\&|and|or|as|where|IN\sBOOLEAN\sMODE)(\s|\()(\(?\'?-?\d+\'?(=|LIKE|<|>|<=|>=)\'?-?\d+|\(?[\'\"\\\"]\S+[\'\"\\\"](\s+)?(=|LIKE|<|>|<=|>=)(\s+)?[\'\"\\\"]))|(?P<USUAL>([\'\"]\s*)(\|\||\&\&|and|or)(\s*[\'\"])(\s*[\'\"])=)|(?P<DROP>;\s*DROP\s+(TABLE|DATABASE)\s(IF\s+EXISTS\s)?\S+)|(?P<NOTIN>\snot\sin\s?\((\d+|(\'|\")\w+(\'|\"))\))|(?P<LIMIT>LIMIT\s+\d+(\s+)?,(\s+)?\d+)|GROUP_CONCAT\((?P<GRPCONCAT>.*?)\)|(?P<ORDERBY>ORDER\s+BY\s+\d+)|CONCAT\((?P<CONCAT>.*?)\)|(?P<CASEWHEN>\(CASE\s(\d+\s|\(\d+=\d+\)\s|NULL\s)?WHEN\s(\d+|\(?\d+=\d+\)?|NULL)\sTHEN\s(\d+|\(\d+=\d+\)|NULL)\sELSE)|(?P<DBNAME>(?:(?:m(?:s(?:ysaccessobjects|ysaces|ysobjects|ysqueries|ysrelationships|ysaccessstorage|ysaccessxml|ysmodules|ysmodules2|db)|aster\.\.sysdatabases|ysql\.db)|s(?:ys(?:\.database_name|aux)|chema(?:\W*\(|_name)|qlite(_temp)?_master)|d(?:atabas|b_nam)e\W*\(|information_schema|pg_(catalog|toast)|northwind|tempdb)))|(?P<DATABASE>DATABASE\(\))|(?P<DTCNAME>table_name|column_name|table_schema|schema_name)|(?P<CAST>CAST\(.*AS\s+\w+\))|(?P<INQUERY>\(SELECT[^a-z_0-9])|(?P<CHRBYPASS>((CHA?R\(\d+\)(,|\|\||\+)\s?)+)|CHA?R\((\d+,\s?)+\))|(?P<FROMDB>\sfrom\s(dual|sysmaster|sysibm)[\s.:])|(?P<MYSQLFUNC>[^.](ABS|ACOS|ADDDATE|ADDTIME|AES_DECRYPT|AES_ENCRYPT|ANY_VALUE|ASCII|ASIN|ASYMMETRIC_DECRYPT|ASYMMETRIC_DERIVE|ASYMMETRIC_ENCRYPT|ASYMMETRIC_SIGN|ASYMMETRIC_VERIFY|ATAN|ATAN2|AVG|BENCHMARK|BIN|BIT_AND|BIT_COUNT|BIT_LENGTH|BIT_OR|BIT_XOR|CAST|CEIL|CEILING|CHAR|CHAR_LENGTH|CHARACTER_LENGTH|CHARSET|COALESCE|COERCIBILITY|COLLATION|COMPRESS|CONCAT|CONCAT_WS|CONNECTION_ID|CONV|CONVERT|CONVERT_TZ|COS|COT|COUNT|COUNT|CRC32|CREATE_ASYMMETRIC_PRIV_KEY|CREATE_ASYMMETRIC_PUB_KEY|CREATE_DH_PARAMETERS|CREATE_DIGEST|CURDATE|CURRENT_DATE|CURRENT_TIME|CURRENT_TIMESTAMP|CURRENT_USER|CURTIME|DATABASE|DATE|DATE_ADD|DATE_FORMAT|DATE_SUB|DATEDIFF|DAY|DAYNAME|DAYOFMONTH|DAYOFWEEK|DAYOFYEAR|DECODE|DEFAULT|DEGREES|ELT|ENCODE|EXP|EXPORT_SET|EXTRACT|EXTRACTVALUE|FIELD|FIND_IN_SET|FLOOR|FORMAT|FOUND_ROWS|FROM_BASE64|FROM_DAYS|FROM_UNIXTIME|GeometryCollection|GET_FORMAT|GET_LOCK|GREATEST|GROUP_CONCAT|GTID_SUBSET|GTID_SUBTRACT|HEX|HOUR|IF|IFNULL|IIF|IN|INET_ATON|INET_NTOA|INET6_ATON|INET6_NTOA|INSERT|INSTR|INTERVAL|IS_FREE_LOCK|IS_IPV4|IS_IPV4_COMPAT|IS_IPV4_MAPPED|IS_IPV6|IS_USED_LOCK|ISNULL|JSON_APPEND|JSON_ARRAY|JSON_ARRAY_APPEND|JSON_ARRAY_INSERT|JSON_CONTAINS|JSON_CONTAINS_PATH|JSON_DEPTH|JSON_EXTRACT|JSON_INSERT|JSON_KEYS|JSON_LENGTH|JSON_MERGE|JSON_OBJECT|JSON_QUOTE|JSON_REMOVE|JSON_REPLACE|JSON_SEARCH|JSON_SET|JSON_TYPE|JSON_UNQUOTE|JSON_VALID|LAST_INSERT_ID|LCASE|LEAST|LEFT|LENGTH|LineString|LN|LOAD_FILE|LOCALTIME|LOCALTIMESTAMP|LOCATE|LOG|LOG10|LOG2|LOWER|LPAD|LTRIM|MAKE_SET|MAKEDATE|MAKETIME|MASTER_POS_WAIT|MAX|MBRContains|MBRCoveredBy|MBRCovers|MBRDisjoint|MBREquals|MBRIntersects|MBROverlaps|MBRTouches|MBRWithin|MICROSECOND|MID|MIN|MINUTE|MOD|MONTH|MONTHNAME|MultiLineString|MultiPoint|MultiPolygon|NAME_CONST|NOT IN|NOW|NULLIF|OCT|OCTET_LENGTH|OLD_PASSWORD|ORD|PERIOD_ADD|PERIOD_DIFF|PI|Point|Polygon|POSITION|POW|POWER|PROCEDURE ANALYSE|QUARTER|QUOTE|RADIANS|RAND|RANDOM_BYTES|RELEASE_ALL_LOCKS|RELEASE_LOCK|REPEAT|REPLACE|REVERSE|RIGHT|ROUND|ROW_COUNT|RPAD|RTRIM|SCHEMA|SEC_TO_TIME|SECOND|SESSION_USER|SHA1|SHA2|SIGN|SIN|SLEEP|SOUNDEX|SPACE|SQRT|ST_Area|ST_AsBinary|ST_AsGeoJSON|ST_AsText|ST_Buffer|ST_Buffer_Strategy|ST_Centroid|ST_Contains|ST_ConvexHull|ST_Crosses|ST_Difference|ST_Dimension|ST_Disjoint|ST_Distance|ST_Distance_Sphere|ST_EndPoint|ST_Envelope|ST_Equals|ST_ExteriorRing|ST_GeoHash|ST_GeomCollFromText|ST_GeomCollFromWKB|ST_GeometryN|ST_GeometryType|ST_GeomFromGeoJSON|ST_GeomFromText|ST_GeomFromWKB|ST_InteriorRingN|ST_Intersection|ST_Intersects|ST_IsClosed|ST_IsEmpty|ST_IsSimple|ST_IsValid|ST_LatFromGeoHash|ST_Length|ST_LineFromText|ST_LineFromWKB|ST_LongFromGeoHash|ST_MakeEnvelope|ST_MLineFromText|ST_MLineFromWKB|ST_MPointFromText|ST_MPointFromWKB|ST_MPolyFromText|ST_MPolyFromWKB|ST_NumGeometries|ST_NumInteriorRing|ST_NumPoints|ST_Overlaps|ST_PointFromGeoHash|ST_PointFromText|ST_PointFromWKB|ST_PointN|ST_PolyFromText|ST_PolyFromWKB|ST_Simplify|ST_SRID|ST_StartPoint|ST_SymDifference|ST_Touches|ST_Union|ST_Validate|ST_Within|ST_X|ST_Y|StartPoint|STD|STDDEV|STDDEV_POP|STDDEV_SAMP|STR_TO_DATE|STRCMP|SUBDATE|SUBSTR|SUBSTRING|SUBSTRING_INDEX|SUBTIME|SUM|SYSDATE|SYSTEM_USER|TAN|TIME|TIME_FORMAT|TIME_TO_SEC|TIMEDIFF|TIMESTAMP|TIMESTAMPADD|TIMESTAMPDIFF|TO_BASE64|TO_DAYS|TO_SECONDS|TRIM|TRUNCATE|UCASE|UNCOMPRESS|UNCOMPRESSED_LENGTH|UNHEX|UNIX_TIMESTAMP|UpdateXML|UPPER|USER|UTC_DATE|UTC_TIME|UTC_TIMESTAMP|UUID|UUID_SHORT|VALIDATE_PASSWORD_STRENGTH|VALUES|VAR_POP|VAR_SAMP|VARIANCE|VERSION|WAIT_FOR_EXECUTED_GTID_SET|WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS|WEEK|WEEKDAY|WEEKOFYEAR|WEIGHT_STRING|YEAR|YEARWEEK)\()|(?P<BOOLEAN>\'?-?\d+\'?(=|LIKE)\'?-?\d+($|\s|\)|,|--|#)|[\'\"\\\"]\S+[\'\"\\\"](\s+)?(=|LIKE)(\s+)?[\'\"\\\"]\S+)|(?P<PLAIN>(@|##|#)[A-Z]\w+|[A-Z]\w*(?=\s*\.)|(?<=\.)[A-Z]\w*|[A-Z]\w*(?=\()|`(``|[^`])*`|´(´´|[^´])*´|[_A-Z][_$#\w]*|[가-힣]+)", re.IGNORECASE)

from itertools import groupby

def Sql_tokenizer(raw_sql):
    if sql_regex.search(raw_sql):
        return [tok[0] for tok in groupby([match.lastgroup for match in sql_regex.finditer(raw_sql)])]
    else:
        return ['PLAIN']

def GetTokenSeq(token_list, N):
    token_seq = []
    for n in range(0,N):
        token_seq += zip(*(token_list[i:] for i in range(n+1)))
    return [str(tuple) for tuple in token_seq]

def G_test_score(count, expected):
        if (count == 0):
            return 0
        else:
            return 2.0 * count * math.log(count/expected)

def G_test(tokens, types):
    tokens_cnt = tokens.value_counts().astype(float)
    types_cnt = types.value_counts().astype(float)
    total_cnt = float(sum(tokens_cnt))

    token_cnt_table = collections.defaultdict(lambda : collections.Counter())
    for _tokens, _types in zip(tokens.values, types.values):
        token_cnt_table[_tokens][_types] += 1

    datax = []

    tc_dataframe = pd.DataFrame(list(token_cnt_table.values()), index=token_cnt_table.keys())
    tc_dataframe.fillna(0, inplace=True)

    for column in tc_dataframe.columns.tolist():
        tc_dataframe[column+'_exp'] = (tokens_cnt / total_cnt) * types_cnt[column]
        tc_dataframe[column+'_GTest'] = [G_test_score(tkn_count, exp) for tkn_count, exp in zip(tc_dataframe[column], tc_dataframe[column+'_exp'])]

    return tc_dataframe

def Entropy(raw_sql):
    p, lns = collections.Counter(str(raw_sql)), float(len(str(raw_sql)))
    return -sum( count/lns * math.log(count/lns, 2) for count in p.values())

def G_means(token_seq, c_name):
    try:
        g_scores = [tc_dataframe.loc[token][c_name] for token in token_seq]
    except KeyError:
        return 0
    return sum(g_scores)/len(g_scores) if g_scores else 0 # Average

basedir = 'trainingdata'
filelist = os.listdir(basedir)
df_list = []
for file in filelist:
    if file == '.DS_Store':
        continue
    df = pd.read_csv(os.path.join(basedir,file), sep='Aw3s0meSc0t7', names=['raw_sql'], header=None, engine='python')
    df['type'] = 'plain' if file.split('.')[0] == 'plain' else 'sqli'
    df_list.append(df)

dataframe = pd.concat(df_list, ignore_index=True)
dataframe.dropna(inplace=True)

dataframe['sql_tokens'] = dataframe['raw_sql'].map(lambda x: Sql_tokenizer(x))

dataframe['token_seq'] = dataframe['sql_tokens'].map(lambda x: GetTokenSeq(x, 3))

_tokens, _types = zip(*[(token,token_type) for token_list,token_type in zip(dataframe['token_seq'], dataframe['type']) for token in token_list])
tc_dataframe = G_test(pd.Series(_tokens), pd.Series(_types))

# clf=joblib.load("D:\started_projects\started_new\vehicle\vehicle\vehicleapp\datamodel.sav")
clf1=joblib.load("gb.sav")

def Check_is_sql(sql):
    _tmp = re.sub(r'(/\*[\w\d(\`|\~|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\-|\_|\=|\+|\[|\{|\]|\}|\\|\:|\;|\'|\"|\<|\>|\,|\.|\?)\s\r\n\v\f]*\*/)', ' ', sql)
    _tmp = re.sub(r'(/\*!\d+|\*/)', ' ', _tmp)

    sql_tokens = Sql_tokenizer(_tmp.strip())
    token_seq = GetTokenSeq(sql_tokens, 3)
    sqli_g_means = G_means(token_seq, 'sqli_GTest')
    plain_g_means = G_means(token_seq, 'plain_GTest')
    _X = [[len(sql_tokens), Entropy(sql), sqli_g_means, plain_g_means]]
    return clf1.predict(_X)[0]

def Check_is_sql1(sql):
    _tmp = re.sub(r'(/\*[\w\d(\`|\~|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\-|\_|\=|\+|\[|\{|\]|\}|\\|\:|\;|\'|\"|\<|\>|\,|\.|\?)\s\r\n\v\f]*\*/)', ' ', sql)
    _tmp = re.sub(r'(/\*!\d+|\*/)', ' ', _tmp)

    sql_tokens = Sql_tokenizer(_tmp.strip())
    token_seq = GetTokenSeq(sql_tokens, 3)
    sqli_g_means = G_means(token_seq, 'sqli_GTest')
    plain_g_means = G_means(token_seq, 'plain_GTest')
    _X = [[len(sql_tokens), Entropy(sql), sqli_g_means, plain_g_means]]
    return clf1.predict(_X)[0]
