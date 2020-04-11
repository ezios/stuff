# stuff
Linux input
Connected device , get event number
cat /proc/bus/input/devices 
input event stream
/dev/input/event<n>
-Input event structure
struct input_event
{
   struct timeval time; /* 16 bytes */
   unsigned short type; /* 2 byes */
   unsigned short code; /* 2 bytes*/
   unsigned int value;  /  4 bytes */
};
    
