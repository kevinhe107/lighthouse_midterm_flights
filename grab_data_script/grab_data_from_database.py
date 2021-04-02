import psycopg2

data=None

def grab_sql_data():
    global data
    host = None
    dbname = None
    user = None
    pw = None
    port = None
    query = None

    fh = open('query.txt', 'r')
    
    for line in fh:
        k  = line.split(':=')
        k[1] = k[1].strip()
        if k[0] == 'host':
            host = k[1]
        elif k[0] == 'database':
            dbname = k[1]
        elif k[0] == 'user':
            user = k[1]
        elif k[0] == 'password':
            pw = k[1]
        elif k[0] == 'port':
            port = k[1]
        elif k[0] == 'query':
            query = k[1]
    fh.close()

    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=pw,
        host=host,
        port=port
    )

    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()

def write_sql_fetch():
    global data
    fh = open('data.csv', 'w')
    for i in data:
        for j in i:
            fh.write(f'{j},')
        fh.write("\n")
    fh.close()

if __name__ == '__main__':
    grab_sql_data()
    write_sql_fetch()
