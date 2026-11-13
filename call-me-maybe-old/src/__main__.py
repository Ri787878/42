from call_me_maybe.main import main
import time


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
