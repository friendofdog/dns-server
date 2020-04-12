from modules.classes import Server, Query, QueryHeader, Response


while True:

    # start the server
    server = Server()
    server.start_server()

    # query
    query = Query(server)

    # split response into usable parts
    # each part equal to two bytes in DNS header
    query_header = QueryHeader(query.data[:12])

    # build response piece-by-piece
    response = Response()
    response.build_tid(query_header.tid)
    response.build_flags(query_header.flags)
    response.build_qdcount(query_header.qdcount)
    response.build_ancount(query_header.ancount)
    response.build_nscount(query_header.nscount)
    response.build_arcount(query_header.arcount)
    # response.build_queries(response_data.body)
    print(response)

    # build a response and use sendto() to send response back to addr
    # server.sock.sendto(response, query.addr)
