def compute(n):
    import time, socket
    time.sleep(n)
    host = socket.gethostname()
    return (host, n)

if __name__ == '__main__':
    import dispy, random
    cluster = dispy.JobCluster(compute,nodes=['10.151.32.*','10.151.38.72'],ip_addr='10.151.32.123')
    jobs = []
    for n in range(20):
        job = cluster.submit(random.randint(5,20))
        job.id = n
        jobs.append(job)
    # cluster.wait()
    for job in jobs:
        host, n = job()
        print '%s executed job %s at %s with %s' % (host, job.id, job.start_time, n)
        # other fields of 'job' that may be useful:
        # print job.stdout, job.stderr, job.exception, job.ip_addr, job.start_time, job.end_time
    cluster.stats()
