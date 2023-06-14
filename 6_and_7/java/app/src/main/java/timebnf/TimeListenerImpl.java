package timebnf;

public class TimeListenerImpl extends TimeBaseListener {

    private int minutesAfterMidnight;

    public int getMinutesAfterMidnight() {
        return minutesAfterMidnight;
    }

    public void setMinutesAfterMidnight(int minutesAfterMidnight) {
        this.minutesAfterMidnight = minutesAfterMidnight;
    }


    @Override
    public void enterAm_pm(TimeParser.Am_pmContext ctx) {
        if(ctx.getText().equalsIgnoreCase("pm")){
            minutesAfterMidnight += 12*60;
        }
    }

    @Override
    public void enterHour(TimeParser.HourContext ctx) {
        int hour = Integer.parseInt(ctx.getText());
        if (hour > 23){
            throw new RuntimeException("Error: Hour = " + hour);
        }
        minutesAfterMidnight+= hour * 60;
    }

    @Override
    public void enterMinute(TimeParser.MinuteContext ctx) {
        int minute = Integer.parseInt(ctx.getText());
        if (minute > 59){
            throw new RuntimeException("Error: Minute = " + minute);
        }
        minutesAfterMidnight+=minute;
    }
}
