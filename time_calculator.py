def add_time(start_time, duration_time, starting_day=None):
    start_time = start_time.split()
    
    st_AM_PM = start_time[1]
    st_time = start_time[0].split(':')
    st_time = int(st_time[0]) + int(st_time[1])/60
    
    #convert PM time to 24hrs
    if st_AM_PM == 'PM':
        st_time = st_time+12
    
    dt_time = duration_time.split(':')
    dt_time = int(dt_time[0]) + int(dt_time[1])/60
    
    sum_time = st_time+dt_time
    
    time_dec = sum_time % 24
    hr = int(time_dec)
    m = time_dec-hr
    
    m = int(round(m*60))
    m = f'{m:02d}'
    hr = int(hr)
    
    if time_dec >= 12:
        if hr == 12:
            hr = hr
        else:
            hr = hr-12
        AM_PM = "PM"
    else:
        if hr ==0:
            hr = 12
        AM_PM ="AM"
    
    time = "{hr}:{m} {am_pm}".format(hr=hr,m=m,am_pm=AM_PM)
    
    no_days = int(sum_time/24)
    
    if no_days > 1:
        new_time = "{t} ({d} days later)".format(t=time,d=no_days)
    elif no_days == 1:
        new_time = "{t} (next day)".format(t=time,d=no_days)
    else:
        new_time = time

    if starting_day != None:
        starting_day = starting_day.capitalize()
        days = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
        for k, v in days.items():
            if v==starting_day:
                day_index = k
        
        new_day = no_days + day_index
        new_day = new_day%7
        
        for k, v in days.items():
            if k==new_day:
                day = v
        
        if no_days > 1:
            new_time = "{t}, {day} ({d} days later)".format(t=time,d=no_days, day=day)
        elif no_days == 1:
            new_time = "{t}, {day} (next day)".format(t=time,d=no_days, day=day)
        else:
            new_time = "{t}, {day}".format(day=day, t=time)
        
    return new_time