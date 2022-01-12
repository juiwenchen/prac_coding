// bit shift, AND operation        llen(a)
unsigned short GetBrigtness (unsigned char data[]) {  
    cal_sum = (*data & 0x0F00) + (*data & 0x00F0) + (*data & 0x000F);
    input_sum = data & 0F000;
    if !(cal_sum == input_sum9{
        return 0xFFFF;
    }
    if (data & 0x0F00 != 0x04):
    {
        return 0xFFFF;
    }

    brightness = data[3];
    brightness = brightness >> sizeof(char) + data[2];
}