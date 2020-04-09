from modules.classes import Server, Query, ResponseData, Response


while True:

    # start the server
    server = Server()
    server.start_server()

    # query
    query = Query(server)

    # split response into usable parts
    # each part equal to two bytes in DNS header
    response_data = ResponseData(query.data)

    # build response piece-by-piece
    response = Response()
    response.build_tid(response_data.tid)
    response.build_flags(response_data.flags)
    response.build_qdcount(response_data.qdcount)
    response.build_ancount(response_data.ancount)
    response.build_nscount(response_data.nscount)
    response.build_arcount(response_data.arcount)
    print(response)

    # build a response and use sendto() to send response back to addr
    # server.sock.sendto(response, query.addr)
