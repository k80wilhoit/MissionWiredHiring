import pandas as a
data = pd.read_csv(r'C:Users/katiewilhoit/Downloads/cons.csv')
df = pd.DataFrame(data, columns=[created_dt, updated_dt])
import pandas as b 
df = pd.DataFrame(data, columns=[email])
data = pd.read_csv(r'C:Users/katiewilhoit/Downloads/cons_email.csv')
import pandas as c 
data = pd.read_csv(r'C:Users/katiewilhoit/Downloads/cons_email_chapter_subscription.csv')
df = pd.DataFrame(data, columns=[is_unsub]) 
print (df)