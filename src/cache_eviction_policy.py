import sys
from collections import deque, defaultdict, OrderedDict


# read input file and return k and list of requests
def read_input(filename):
    with open(filename, "r") as f:
        tokens = f.read().split()

    if len(tokens) < 2:
        raise ValueError("File must start with: k m")

    k = int(tokens[0])
    m = int(tokens[1])

    if k < 1:
        raise ValueError("k must be >= 1")
    if m < 0:
        raise ValueError("m must be >= 0")

    request_tokens = tokens[2:]
    if len(request_tokens) != m:
        raise ValueError("Expected {} requests, got {}".format(m, len(request_tokens)))

    requests = []
    for i in request_tokens:
        requests.append(int(i))

    return k, requests


# FIFO: evict the item that was inserted earliest
def count_misses_fifo(k, requests):
    cache_items = set()
    fifo_line = deque()
    misses = 0

    for item in requests:
        if item in cache_items:
            continue

        misses += 1

        if len(cache_items) == k:
            oldest = fifo_line.popleft()
            cache_items.remove(oldest)

        cache_items.add(item)
        fifo_line.append(item)

    return misses


# LRU: evict the item used least recently
def count_misses_lru(k, requests):
    cache = OrderedDict()
    misses = 0

    for item in requests:
        if item in cache:
            cache.move_to_end(item)
        else:
            misses += 1

            if len(cache) == k:
                cache.popitem(last=False)

            cache[item] = True

    return misses


def build_future_positions(requests):
    future = defaultdict(deque)

    for i, item in enumerate(requests):
        future[item].append(i)

    return future


# OPTFF: evict item used farthest in the future
def count_misses_optff(k, requests):
    future = build_future_positions(requests)

    cache_items = set()
    misses = 0

    for i, item in enumerate(requests):
        future[item].popleft()

        if item in cache_items:
            continue

        misses += 1

        if len(cache_items) < k:
            cache_items.add(item)

        else:
            victim = None
            victim_next = -1

            for cached_item in cache_items:

                if len(future[cached_item]) == 0:
                    next_use = float("inf")
                else:
                    next_use = future[cached_item][0]

                if victim is None or next_use > victim_next:
                    victim = cached_item
                    victim_next = next_use

            cache_items.remove(victim)
            cache_items.add(item)

    return misses


def main():
    if len(sys.argv) != 3:
        print("Usage: python cache_eviction_policy.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        k, requests = read_input(input_file)

    except Exception as e:
        print("Error: {}".format(e), file=sys.stderr)
        sys.exit(1)

    fifo = count_misses_fifo(k, requests)
    lru = count_misses_lru(k, requests)
    optff = count_misses_optff(k, requests)

    lines = []
    lines.append("{:<5} : {}".format("FIFO", fifo))
    lines.append("{:<5} : {}".format("LRU", lru))
    lines.append("{:<5} : {}".format("OPTFF", optff))
    output_text = "\n".join(lines)

    print(output_text, end="")

    # write output to file
    with open(output_file, "w") as f:
        f.write(output_text)


if __name__ == "__main__":
    main()
