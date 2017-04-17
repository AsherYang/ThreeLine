package com.asher.threeline.ui.main;

import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.asher.threeline.R;
import com.asher.threeline.db.bean.DbContent;

import java.util.List;

/**
 * Created by ouyangfan on 17/3/22.
 * <p>
 * Adapter
 */
public class MainAdapter extends RecyclerView.Adapter<RecyclerView.ViewHolder> {

    private Context mContext;
    private List<DbContent> mData;

    public MainAdapter(Context context, List<DbContent> list) {
        this.mContext = context;
        mData = list;
    }

    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(mContext).inflate(R.layout.item_rv_main, parent, false);
        return new MyViewHolder(view);
    }

    @Override
    public void onBindViewHolder(RecyclerView.ViewHolder holder, int position) {
        DbContent content = mData.get(position);
        String str = content.getSongName() + " syncKey = "+ content.getSyncKey();
        ((MyViewHolder) holder).name.setText(str);
    }

    @Override
    public int getItemCount() {
        return mData.size();
    }

    class MyViewHolder extends RecyclerView.ViewHolder {

        private final TextView name;

        public MyViewHolder(View itemView) {
            super(itemView);
            name = (TextView) itemView.findViewById(R.id.tv_item_name);
        }
    }

}
