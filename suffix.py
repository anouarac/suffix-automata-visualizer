import graphviz

to = []
lens, link, lasts = [], [], []
small, big = [], []
cur, last = 0, 0

def init():
    global to, link, lens, link, lasts, small, big, cur, last
    to = []
    lens, link, lasts = [], [], []
    small, big, = [], []
    cur, last = 0, 0
    link.append(-1)
    lens.append(0)
    to.append({})
    lasts.append(-1)
    small.append("")
    big.append("")

def addchar(c):
    global to, link, lens, link, lasts, small, big, cur, last
    last = cur
    cur = len(lens)
    lens.append(lens[last]+1)
    link.append(0)
    lasts.append(last)
    to.append({})
    big.append(big[last]+c)
    small.append(small[last]+c)

    p = last
    while p >= 0 and c not in to[p]:
        to[p][c] = cur;
        if len(small[p])+1 < len(small[cur]):
            small[cur] = small[p]+c
        p = link[p]

    if p == -1:
        return

    q = to[p][c]
    if lens[q] == lens[p]+1:
        link[cur] = q
    else:
        clone = len(lens)
        lens.append(lens[p]+1)
        link.append(link[q])
        to.append(to[q].copy())
        small.append(small[p]+c)
        big.append(big[p]+c)
        link[cur],link[q] = clone,clone
        lasts.append(p);
        while p >= 0 and to[p][c] == q:
            to[p][c] = clone
            if len(small[p])+1 < len(small[clone]):
                small[clone] = small[p]+c
            p = link[p]

def insert(s):
    init()
    for c in s:
        addchar(c)

def g_label(u):
    if u == 0:
        return "0"
    global big, small
    return big[u]+'\n\n'+small[u]

vis = []

def dfs(u, graph, show_links):
    if vis[u]:
        return
    vis[u] = True
    for c in to[u].keys():
        graph.edge(g_label(u), g_label(to[u][c]), label=c)
        dfs(to[u][c], graph, show_links)
    if link[u] != -1 and show_links:
        graph.edge(g_label(u), g_label(link[u]), color='blue', constraint='false')


def gen(s, show_links):
    insert(s)

    graph = graphviz.Digraph("G", filename="./graph")
    graph.attr(rankdir='LR', size='8,5', ordering='out', label="Fig. "+s+"'s suffix automaton")

    graph.attr('node', shape='doublecircle', color='red')
    global cur, link, big, small
    terminal = cur
    while cur > -1:
        graph.node(g_label(cur))
        cur = link[cur]
    graph.node("", shape='none')
    graph.edge("", "0")
    graph.attr('node', shape='circle', color='black')
    global vis
    vis = [False] * len(lens)
    dfs(0, graph, show_links)
    graph.render()
