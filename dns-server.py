from modules.classes import Server, Query, QueryHeader, QueryBody, Response


while True:

    # start the server
    server = Server()
    server.start_server()

    # query
    query = Query(server)

    # split response into usable parts
    # first 12 bytes for header, rest for body
    query_header = QueryHeader(query.data[:12])
    query_body = QueryBody(query.data[12:])

    # build response piece-by-piece
    response = Response()
    response.build_tid(query_header.tid)
    response.build_flags(query_header.flags)
    response.build_qdcount(query_header.qdcount)
    response.build_ancount(query_header.ancount)
    response.build_nscount(query_header.nscount)
    response.build_arcount(query_header.arcount)
    print(response)

    # build a response and use sendto() to send response back to addr
    # server.sock.sendto(response, query.addr)
