package com.asher.threeline.ui.test;

import android.content.Context;
import android.util.AttributeSet;
import android.util.Log;
import android.view.GestureDetector;
import android.view.LayoutInflater;
import android.view.MotionEvent;
import android.view.View;
import android.view.ViewConfiguration;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.Scroller;

import com.asher.threeline.R;

/**
 * Created by ouyangfan on 17/3/30.
 */
public class HangUpBtn extends RelativeLayout implements GestureDetector.OnGestureListener {

    private static final String TAG = HangUpBtn.class.getSimpleName();
    private ImageView mCircle;
    private ImageView mHang;
    // 最后点击的点
    private float mLastMotionY;
    private Scroller mScroller;
    private GestureDetector detector;
    private final static int TOUCH_STATE_REST = 0;
    private final static int TOUCH_STATE_SCROLLING = 1;
    private int mTouchState = TOUCH_STATE_REST;
    private int mTouchSlop;
    int move = 0;// 移动距离
    int MAXMOVE = 850;// 最大允许的移动距离
    int up_excess_move = 0;// 往上多移的距离
    int down_excess_move = 0;// 往下多移的距离

    public HangUpBtn(Context context) {
        this(context, null);
    }

    public HangUpBtn(Context context, AttributeSet attrs) {
        this(context, attrs, 0);
    }

    public HangUpBtn(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        initView(context);
        init(context);
    }

    private void initView(Context context) {
        View view = LayoutInflater.from(context).inflate(R.layout.layout_hang_up, this, true);
        mCircle = (ImageView) view.findViewById(R.id.iv_circle);
        mHang = (ImageView) view.findViewById(R.id.iv_hang);
    }

    private void init(Context context) {
        mScroller = new Scroller(context);
        detector = new GestureDetector(context, this);
        final ViewConfiguration configuration = ViewConfiguration.get(context);
        // 获得可以认为是滚动的距离
        mTouchSlop = configuration.getScaledTouchSlop();
    }

    @Override
    public void computeScroll() {
        if (mScroller.computeScrollOffset()) {
            scrollTo(0, mScroller.getCurrY());
            postInvalidate();
        }
    }

    @Override
    public boolean onInterceptTouchEvent(MotionEvent event) {
        final int action = event.getAction();
        final float y = event.getY();
        switch (action) {
            case MotionEvent.ACTION_DOWN:
                mLastMotionY = y;
                mTouchState = mScroller.isFinished() ? TOUCH_STATE_REST : TOUCH_STATE_SCROLLING;
                break;
            case MotionEvent.ACTION_MOVE:
                final int yDiff = (int) Math.abs(y - mLastMotionY);
                Log.i(TAG, " mLastMotionY = " + mLastMotionY + " , Y = " + y);
                boolean yMoved = yDiff > mTouchSlop;
                if (yMoved) {
                    mTouchState = TOUCH_STATE_SCROLLING;
                }
                break;
            case MotionEvent.ACTION_UP:
                mTouchState = TOUCH_STATE_REST;
                break;
        }
        return mTouchState != TOUCH_STATE_REST;
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        final float y = event.getY();
        switch (event.getAction()) {
            case MotionEvent.ACTION_DOWN:
                if (!mScroller.isFinished()) {
                    mScroller.forceFinished(true);
                    move = mScroller.getFinalY();
                }
                mLastMotionY = y;
                break;
            case MotionEvent.ACTION_MOVE:
                if (event.getPointerCount() == 1) {
                    // 随手指 拖动的代码
                    int deltaY = 0;
                    deltaY = (int) (mLastMotionY - y);
                    mLastMotionY = y;
                    Log.d("move", "" + move);
                    if (deltaY < 0) {
                        // 下移
                        // 判断上移 是否滑过头
                        if (up_excess_move == 0) {
                            if (move > 0) {
                                int move_this = Math.max(-move, deltaY);
                                move = move + move_this;
                                scrollBy(0, move_this);
                            } else if (move == 0) {// 如果已经是最顶端 继续往下拉
                                Log.d("down_excess_move", "" + down_excess_move);
                                down_excess_move = down_excess_move - deltaY / 2;// 记录下多往下拉的值
                                scrollBy(0, deltaY / 2);
                            }
                        } else if (up_excess_move > 0)// 之前有上移过头
                        {
                            if (up_excess_move >= (-deltaY)) {
                                up_excess_move = up_excess_move + deltaY;
                                scrollBy(0, deltaY);
                            } else {
                                up_excess_move = 0;
                                scrollBy(0, -up_excess_move);
                            }
                        }
                    } else if (deltaY > 0) {
//                        return detector.onTouchEvent(event);
                        // 上移
                        if (down_excess_move == 0) {
                            if (MAXMOVE - move > 0) {
                                int move_this = Math.min(MAXMOVE - move, deltaY);
                                move = move + move_this;
                                scrollBy(0, move_this);
                            } else if (MAXMOVE - move == 0) {
                                if (up_excess_move <= 100) {
                                    up_excess_move = up_excess_move + deltaY / 2;
                                    scrollBy(0, deltaY / 2);
                                }
                            }
                        } else if (down_excess_move > 0) {
                            if (down_excess_move >= deltaY) {
                                down_excess_move = down_excess_move - deltaY;
                                scrollBy(0, deltaY);
                            } else {
                                down_excess_move = 0;
                                scrollBy(0, down_excess_move);
                            }
                        }
                    }
                }
                break;
            case MotionEvent.ACTION_UP:
                // 多滚是负数 记录到move里
                if (up_excess_move > 0) {
                    // 多滚了 要弹回去
                    scrollBy(0, -up_excess_move);
                    invalidate();
                    up_excess_move = 0;
                }
                if (down_excess_move > 0) {
                    // 多滚了 要弹回去
                    scrollBy(0, down_excess_move);
                    invalidate();
                    down_excess_move = 0;
                }
                mTouchState = TOUCH_STATE_REST;
                break;
        }
        return this.detector.onTouchEvent(event);
    }

    @Override
    public boolean onDown(MotionEvent motionEvent) {
        return true;
    }

    @Override
    public void onShowPress(MotionEvent motionEvent) {

    }

    @Override
    public boolean onSingleTapUp(MotionEvent motionEvent) {
        return false;
    }

    @Override
    public boolean onScroll(MotionEvent motionEvent, MotionEvent motionEvent1, float v, float v1) {
        return false;
    }

    @Override
    public void onLongPress(MotionEvent motionEvent) {

    }

    @Override
    public boolean onFling(MotionEvent motionEvent, MotionEvent motionEvent1, float velocityX, float velocityY) {
        //随手指 快速拨动的代码
        Log.i(TAG, "onFling");
        if (up_excess_move == 0 && down_excess_move == 0) {
            int slow = -(int) velocityY * 3 / 4;
            mScroller.fling(0, move, 0, slow, 0, 0, 0, MAXMOVE);
            move = mScroller.getFinalY();
            computeScroll();
        }
        return false;
    }
}
