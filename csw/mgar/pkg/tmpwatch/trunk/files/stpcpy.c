char *                                                                                    
stpcpy(char *a,const char *b)                                                             
{                                                                                         
    while( *b )                                                                           
    *a++ = *b++;                                                                          
    *a = 0;                                                                               
                                                                                          
    return (char*)a;                                                                      
}                     
