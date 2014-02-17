# specifying configuration parameters in one place

# dummy function to do a database call
def db_query(userid, password, query_str):
    #conn = get_conn(userid, password)
    #conn.execute(query_str)
    print("query {0} using {1}".format(query_str, userid))
    

def query_executor(userid, password):
    #conn = get_conn(userid, password)
    def query_performer(query_str):
        #conn.execute(query_str)
        print("query {0} using {1}".format(query_str, userid))
    return query_performer


querying = query_executor("myid", "mypassword")

querying("select foo from bar")
querying("select baz from buz")

# Similarly you could use it for dependency injection
# Also for temporal separation etc.