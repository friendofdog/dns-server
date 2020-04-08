from modules.classes import Server, Query, ResponseData, Response


while True:

    # start the server
    server = Server()
    server.start_server()

    # query
    query = Query(server)

    response_data = ResponseData(query.data)

    response = Response()
    response.build_tid(response_data.tid)
    response.build_flags(response_data.flags)
    print(response)

    # build a response and use sendto() to send response back to addr
    # server.sock.sendto(response, query.addr)
