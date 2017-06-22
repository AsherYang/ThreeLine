package com.asher.threeline.ui.view;

import android.content.Context;
import android.content.res.TypedArray;
import android.graphics.Canvas;
import android.graphics.Path;
import android.graphics.Rect;
import android.util.AttributeSet;
import android.widget.TextView;

import com.asher.threeline.R;

/**
 * Created by ouyangfan on 17/6/4.
 * <p>
 * vertical text view
 */
public class VerticalTextView extends TextView {

    // 文本方向
    private int direction;
    // 4个方向值
    public final static int ORIENTATION_UP_TO_DOWN = 0;
    public final static int ORIENTATION_DOWN_TO_UP = 1;
    public final static int ORIENTATION_LEFT_TO_RIGHT = 2;
    public final static int ORIENTATION_RIGHT_TO_LEFT = 3;
    private Rect text_bounds = new Rect();
    private Path path = new Path();

    public VerticalTextView(Context context) {
        this(context, null);
    }

    public VerticalTextView(Context context, AttributeSet attrs) {
        this(context, attrs, 0);
    }

    public VerticalTextView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);

        initAttr(context, attrs);
    }

    private void initAttr(Context context, AttributeSet attrs) {
        TypedArray a = context.obtainStyledAttributes(attrs, R.styleable.VerticalTextView);
        direction = a.getInt(R.styleable.VerticalTextView_textDirection, 0);
        a.recycle();

        requestLayout();
        invalidate();
    }

    public void setDirection(int direction) {
        this.direction = direction;

        requestLayout();
        invalidate();
    }

    @Override
    protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
        getPaint().getTextBounds(getText().toString(), 0, getText().length(), text_bounds);
        switch (direction) {
            case ORIENTATION_LEFT_TO_RIGHT:
            case ORIENTATION_RIGHT_TO_LEFT:
                setMeasuredDimension(measureHeight(widthMeasureSpec), measureWidth(heightMeasureSpec));
                break;
            case ORIENTATION_UP_TO_DOWN:
            case ORIENTATION_DOWN_TO_UP:
            default:
                setMeasuredDimension(measureWidth(widthMeasureSpec), measureHeight(heightMeasureSpec));
                break;
        }
    }

    private int measureWidth(int measureSpec) {
        int result = 0;
        int specMode = MeasureSpec.getMode(measureSpec);
        int specSize = MeasureSpec.getSize(measureSpec);

        if (specMode == MeasureSpec.EXACTLY) {
            result = specSize;
        } else {
            result = text_bounds.height() + getPaddingTop() + getPaddingBottom();
            if (specMode == MeasureSpec.AT_MOST) {
                result = Math.min(result, specSize);
            }
        }
        return result;
    }

    private int measureHeight(int measureSpec) {
        int result = 0;
        int specMode = MeasureSpec.getMode(measureSpec);
        int specSize = MeasureSpec.getSize(measureSpec);

        if (specMode == MeasureSpec.EXACTLY) {
            result = specSize;
        } else {
            result = text_bounds.width() + getPaddingLeft() + getPaddingRight();
            if (specMode == MeasureSpec.AT_MOST) {
                result = Math.min(result, specSize);
            }
        }
        return result;
    }

    @Override
    protected void onDraw(Canvas canvas) {
//        super.onDraw(canvas);

        canvas.save();
        int startX = 0;
        int startY = 0;
        int stopX = 0;
        int stopY = 0;

        if (direction == ORIENTATION_UP_TO_DOWN) {
            startX = (getWidth() - text_bounds.height() >> 1);
            startY = (getHeight() - text_bounds.width() >> 1);
            stopX = (getWidth() - text_bounds.height() >> 1);
            stopY = (getHeight() + text_bounds.width() >> 1);
            path.moveTo(startX, startY);
            path.lineTo(stopX, stopY);
//            Log.i("VTV", " startX " + startX + " , startY = " + startY + " , stopX = " + stopX +
//                    " , stopY = " + stopY + " , getWidth = " + getWidth());
//            Log.i("VTV", "  TxHeight = " + text_bounds.height() + " , 》" + (text_bounds.height() >> 1));
        } else if (direction == ORIENTATION_DOWN_TO_UP) {
            startX = (getWidth() + text_bounds.height() >> 1);
            startY = (getHeight() + text_bounds.width() >> 1);
            stopX = (getWidth() + text_bounds.height() >> 1);
            stopY = (getHeight() - text_bounds.width() >> 1);
            path.moveTo(startX, startY);
            path.lineTo(stopX, stopY);
        } else if (direction == ORIENTATION_LEFT_TO_RIGHT) {
            startX = (getWidth() - text_bounds.width() >> 1);
            startY = (getHeight() + text_bounds.height() >> 1);
            stopX = (getWidth() + text_bounds.width() >> 1);
            stopY = (getHeight() + text_bounds.height() >> 1);
            path.moveTo(startX, startY);
            path.lineTo(stopX, stopY);
        } else if (direction == ORIENTATION_RIGHT_TO_LEFT) {
            startX = (getWidth() + text_bounds.width() >> 1);
            startY = (getHeight() - text_bounds.height() >> 1);
            stopX = (getWidth() - text_bounds.width() >> 1);
            stopY = (getHeight() - text_bounds.height() >> 1);
            path.moveTo(startX, startY);
            path.lineTo(stopX, stopY);
        }
        this.getPaint().setColor(this.getCurrentTextColor());
        canvas.drawTextOnPath(getText().toString(), path, 0, 0, this.getPaint());
        canvas.restore();
    }
}
