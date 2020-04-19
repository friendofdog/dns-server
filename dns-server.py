import sys
from dns import *

if len(sys.argv) != 2:
    raise RuntimeError('XXX write code to handle command line arguments')

while True:

    # get zones included in /zones
    zones = Zones()

    # start the server
    server = Server()
    server.start_server()

    # query
    query = Query(server)

    # split response into usable parts
    # first 12 bytes for header, rest for body
    query_header = QueryHeader(query.data[:12])
    query_body = QueryBody(query.data[12:])
    print(query_header)
    print(query_body)

    response = ResponseHeader(query_header)
    print(response)


    response.build_tid(query_header.tid)
    response.build_flags(query_header.flags)
    response.build_qdcount(query_header.qdcount)
    response.build_ancount(zones.zones, query_body.qname, query_body.qtype)
    response.build_nscount(query_header.nscount)
    response.build_arcount(query_header.arcount)
    print(response)

    # build a response and use sendto() to send response back to addr
    # server.sock.sendto(response, query.addr)

