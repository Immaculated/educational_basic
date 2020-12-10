h_start_1, m_start_1, s_start_1 = map(int, input('enter hours, minutes and seconds of start of 1st event\n').split(':'))
h_finish_1, m_finish_1, s_finish_1 = map(int, input('enter hours, minutes and seconds of end of 1st event\n').split(':'))
h_start_2, m_start_2, s_start_2 = map(int, input('enter hours, minutes and seconds of start of 2nd event\n').split(':'))
h_finish_2, m_finish_2, s_finish_2 = map(int, input('enter hours, minutes and seconds of end of 2nd event\n').split(':'))
start1 = h_start_1 * 3600 + m_start_1 * 60 + s_start_1
start2 = h_start_2 * 3600 + m_start_2 * 60 + s_start_2
finish1 = h_finish_1 * 3600 + m_finish_1 * 60 + s_finish_1
finish2 = h_finish_2 * 3600 + m_finish_2 * 60 + s_finish_2
print(True if (start1 - finish2) * (start2 - finish1) > 0 else False)